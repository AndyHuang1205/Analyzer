import os

import openpyxl
import pandas as pd


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
    # Add some data
    data = returnCSVData().values
    # Write data to the sheet
    for row in data:
        sheet.append(row.tolist())

    # # Save the workbook to a file
    wb.save(file_name)
    print(f"Excel file '{file_name}' created successfully!")

