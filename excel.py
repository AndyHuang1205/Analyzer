import os

import matplotlib.pyplot as plt
import openpyxl
import pandas as pd
from openpyxl import load_workbook
from openpyxl.drawing.image import Image
from temp import get_temperature
import xlsxwriter


# def getGraph(pivot_table, value, graphTitle, xLabel, yLabel=None, rotate=90, fontSize=8):
#     if yLabel is not None:
#         yLabel = value
#     plt.figure(figsize=(8, 5))
#     plt.plot(pivot_table.index, pivot_table[value], marker='o', linestyle='-', color='b')
#
#     # Labels and Title
#     plt.xlabel(xLabel)
#     plt.ylabel(yLabel)
#     plt.title(graphTitle)
#     plt.xticks(rotation=rotate, fontsize=fontSize)
#     plt.tight_layout()
#     plot_filename = "pivot_chart.png"
#     plt.savefig(plot_filename)
#     plt.close()
#
#     # Show the graph
#     wb = load_workbook("test.xlsx")  # TODO change name
#     ws = wb.create_sheet(graphTitle)
#     # ws = wb["TimeTable"]
#     img = Image(plot_filename)
#     ws.add_image(img, "C1")
#     wb.save("test.xlsx")


# returns either an error string or data
def returnCSVData():
    upload_directory = "uploaded_files"

    # Ensure the directory exists
    if not os.path.exists(upload_directory):
        return "No uploaded_files directory found."
    else:
        # List all files in the directory
        files = [f for f in os.listdir(upload_directory) if f.endswith('.csv')]
        datas = []
        if not files:
            return "No CSV files found in the uploaded_files directory."
        else:
            for file in files:
                file_path = os.path.join(upload_directory, file)
                try:
                    # Read the CSV file
                    df = pd.read_csv(file_path, skiprows=6)
                    datas.append(df)
                except Exception as e:
                    return f"Error reading {file}: {e}"
            return pd.concat(datas, ignore_index=True)


def create_excel_file(file_name):
    # Create a new workbook
    wb = openpyxl.Workbook()
    # Select the active sheet
    sheet = wb.active
    sheet.title = "Data"
    sheet.append(returnCSVData().columns.tolist())
    # Add column headers

    # Add some data
    data = returnCSVData().values
    # Write data to the sheet
    for row in data:
        sheet.append(row.tolist())

    # # Save the workbook to a file
    wb.save(file_name)
    print(f"Excel file '{file_name}' created successfully!")





# Function to upload CSV file
# def upload_csv():
#     # Open file dialog to choose CSV file
#     file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
#
#     if file_path:
#         clear_directory("uploaded_files")
#         # Define the directory to save the file
#         save_directory = os.path.expanduser("uploaded_files")
#
#         # Create directory if it does not exist
#         if not os.path.exists(save_directory):
#             os.makedirs(save_directory)
#
#         # Get the file name from the path
#         file_name = os.path.basename(file_path)
#
#         # Define the path to save the file
#         save_path = os.path.join(save_directory, file_name)
#
#         # Copy the uploaded file to the save path
#         try:
#             shutil.copy(file_path, save_path)
#             print(f"CSV file uploaded and saved successfully to {save_path}")
#         except Exception as e:
#             print(f"Error saving the file: {e}")
#     else:
#         print("No file selected.")




# plt.figure(figsize=(8, 5))
# plt.plot(time_usage_table.index, time_usage_table['USAGE (kWh)'], marker='o', linestyle='-', color='b')

# Labels and Title

# plt.xlabel("Time")
# plt.ylabel("Usage")
# plt.title("Usage by Time")
# plt.xticks(rotation=90, fontsize=8)
# plt.tight_layout()
# plot_filename = "pivot_chart.png"
# plt.savefig(plot_filename)
# plt.close()
#
# # Show the graph
# wb = load_workbook("test.xlsx")  # TODO change name
# ws = wb.create_sheet("Graphs")
# # ws = wb["TimeTable"]
# img = Image(plot_filename)
# ws.add_image(img, "A1")
#
# wb.save("test.xlsx")
