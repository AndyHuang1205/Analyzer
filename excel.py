import os

import matplotlib.pyplot as plt
import openpyxl
import pandas as pd
from openpyxl import load_workbook
from openpyxl.drawing.image import Image
from temp import get_temperature
from multiprocessing import Pool


def getGraph(pivot_table, value, graphTitle, xLabel, yLabel=None, rotate=90, fontSize=8):
    if yLabel is not None:
        yLabel = value
    plt.figure(figsize=(8, 5))
    plt.plot(pivot_table.index, pivot_table[value], marker='o', linestyle='-', color='b')

    # Labels and Title
    plt.xlabel(xLabel)
    plt.ylabel(yLabel)
    plt.title(graphTitle)
    plt.xticks(rotation=rotate, fontsize=fontSize)
    plt.tight_layout()
    plot_filename = "pivot_chart.png"
    plt.savefig(plot_filename)
    plt.close()

    # Show the graph
    wb = load_workbook("test.xlsx")  # TODO change name
    ws = wb.create_sheet(graphTitle)
    # ws = wb["TimeTable"]
    img = Image(plot_filename)
    ws.add_image(img, "C1")
    wb.save("test.xlsx")


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


# print(returnCSVData().columns)
df = returnCSVData()
# create_excel_file("test.xlsx")

date_usage_table = pd.pivot_table(returnCSVData(),
                                  values='USAGE (kWh)',  # Columns to aggregate
                                  index='DATE',
                                  fill_value=0,
                                  aggfunc='sum',
                                  ).reset_index()

time_usage_table = pd.pivot_table(returnCSVData(),
                                  values='USAGE (kWh)',  # Columns to aggregate
                                  index='START TIME',
                                  fill_value=0,
                                  aggfunc='mean',
                                  ).reset_index()
# with Pool(2) as pool:
    # date_usage_table["High"] = pool.map(get_temperature, date_usage_table["DATE"])
date_usage_table["Low"] = date_usage_table["DATE"].map(lambda x: get_temperature(x)[0])
date_usage_table["Low"] = date_usage_table["DATE"].map(lambda x: get_temperature(x)[1])
print(date_usage_table.head())


with pd.ExcelWriter('test.xlsx', engine='openpyxl') as writer:
    # Write the original dataframe to the first sheet
    df.to_excel(writer, sheet_name='Data', index=False)

    # Write the pivot table to the second sheet
    date_usage_table.to_excel(writer, sheet_name='PivotTable')

    time_usage_table.to_excel(writer, sheet_name='TimeTable')

getGraph(time_usage_table, 'USAGE (kWh)', "Usage by Time", "Time", "Usage", fontSize=6)
getGraph(date_usage_table, 'USAGE (kWh)', "Daily Usage", "Day", "Usage")

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


