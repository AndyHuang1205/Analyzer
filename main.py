from downloadRequirements import install
from interface import createMainWindow
from excel import returnCSVData
from temp import get_temperature

# install()

import pandas as pd

createMainWindow()

# print(returnCSVData().columns)
df = returnCSVData()
# create_excel_file("test.xlsx")
print(df)
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
#     date_usage_table["High"] = pool.map(get_temperature, date_usage_table["DATE"])
date_usage_table["High"] = date_usage_table["DATE"].map(lambda x: get_temperature(x)[0])
date_usage_table["Low"] = date_usage_table["DATE"].map(lambda x: get_temperature(x)[1])

with pd.ExcelWriter('test.xlsx', engine='openpyxl') as writer:
    # Write the original dataframe to the first sheet
    df.to_excel(writer, sheet_name='Data', index=False)

    # Write the pivot table to the second sheet
    date_usage_table.to_excel(writer, sheet_name='DateTable')

    time_usage_table.to_excel(writer, sheet_name='TimeTable', index=False)
    print("Completed")
# getGraph(time_usage_table, 'USAGE (kWh)', "Usage by Time", "Time", "Usage", fontSize=6)
# getGraph(date_usage_table, 'USAGE (kWh)', "Daily Usage", "Day", "Usage")
