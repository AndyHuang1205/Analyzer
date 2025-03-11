import tkinter as tk
from tkinter import filedialog
import pandas as pd
import os
import shutil
import openpyxl
import excel


def clear_directory(directory_path):
    try:
        # Check if the directory exists
        if os.path.exists(directory_path):
            # Iterate over all files and subdirectories in the directory
            for filename in os.listdir(directory_path):
                file_path = os.path.join(directory_path, filename)

                # If it's a file, delete it
                if os.path.isfile(file_path):
                    os.remove(file_path)
                    print(f"Deleted file: {file_path}")

                # If it's a directory, remove it recursively
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
                    print(f"Deleted directory: {file_path}")

            print(f"All files and subdirectories in '{directory_path}' have been cleared.")
        else:
            print(f"Directory '{directory_path}' does not exist.")

    except Exception as e:
        print(f"Error clearing the directory: {e}")


# Function to upload CSV file
def upload_csv():
    # Open file dialog to choose CSV file
    file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])

    if file_path:
        # Define the directory to save the file
        save_directory = os.path.expanduser("uploaded_files")

        # Create directory if it does not exist
        if not os.path.exists(save_directory):
            os.makedirs(save_directory)

        # Get the file name from the path
        file_name = os.path.basename(file_path)

        # Define the path to save the file
        save_path = os.path.join(save_directory, file_name)

        # Copy the uploaded file to the save path
        try:
            shutil.copy(file_path, save_path)
            print(f"CSV file uploaded and saved successfully to {save_path}")
        except Exception as e:
            print(f"Error saving the file: {e}")
    else:
        print("No file selected.")


def upload_csvs():
    # Open file dialog to choose CSV file
    file_paths = filedialog.askopenfilenames(filetypes=[("CSV files", "*.csv")])

    if file_paths:
        # Define the directory to save the file
        save_directory = os.path.expanduser("uploaded_files")

        # Create directory if it does not exist
        if not os.path.exists(save_directory):
            os.makedirs(save_directory)

        for file_path in file_paths:
            # Get the file name from the path
            file_name = os.path.basename(file_path)

            # Define the path to save the file
            save_path = os.path.join(save_directory, file_name)

            # Copy the uploaded file to the save path
            try:
                shutil.copy(file_path, save_path)
                print(f"CSV file uploaded and saved successfully to {save_path}")
            except Exception as e:
                print(f"Error saving the file {file_name}: {e}")
    else:
        print("No file selected.")


def center_window(window, width, height):
    # Get the screen width and height
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    # Calculate the x and y coordinates to center the window
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)

    # Set the window size and position
    window.geometry(f'{width}x{height}+{x}+{y}')
    root.deiconify()


# Create the main window
os.environ["TK_SILENCE_DEPRECATION"] = "1"
root = tk.Tk()
root.title("CSV File Upload")
root.withdraw()
# Set the window size
window_width = 400
window_height = 200
# Center the window
center_window(root, window_width, window_height)
root.focus_force()

# Create a button that allows the user to upload a CSV file
# upload_button = tk.Button(root, text="Upload File", command=upload_csv, width=20, )
# upload_button1 = tk.Button(root, text="Upload Multiple Files", command=upload_csvs, width=20)
# upload_button.pack(pady=20)
# upload_button1.pack()
# root.lift()
# file_name = "example_data.xlsx"
# create_excel_file(file_name)

# Start the Tkinter event loop
root.mainloop()
