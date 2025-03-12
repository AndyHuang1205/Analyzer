import shutil
import os
from setup import install
from interface import createMainWindow
from excel import returnCSVData
from temperature import get_temperature
install()
import pandas as pd

createMainWindow()

df = returnCSVData()

date_usage_table = pd.pivot_table(df,
                                  values='USAGE (kWh)',  # Columns to aggregate
                                  index='DATE',
                                  fill_value=0,
                                  aggfunc='sum',
                                  ).reset_index()

time_usage_table = pd.pivot_table(df,
                                  values='USAGE (kWh)',  # Columns to aggregate
                                  index='START TIME',
                                  fill_value=0,
                                  aggfunc='mean',
                                  ).reset_index().round({'USAGE (kWh)': 2})


date_usage_table[["High", "Low"]] = date_usage_table["DATE"].apply(lambda x: pd.Series(get_temperature(x)))
# Path to the Downloads folder
downloads_path = os.path.join(os.path.expanduser("~"), "Downloads")

# Save the file in the Downloads folder
file_path = os.path.join(downloads_path, 'EnergyData.xlsx')

with pd.ExcelWriter(file_path) as writer:
    df.to_excel(writer, sheet_name='Data', index=False)
    date_usage_table.to_excel(writer, sheet_name='DateTable', index=False)
    time_usage_table.to_excel(writer, sheet_name='Usage by Time', index=False)
    print("Completed")
    shutil.rmtree("uploaded_files")
