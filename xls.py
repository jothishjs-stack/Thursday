from openpyxl import Workbook
from tuples import list_devices
wb=Workbook()
ws=wb.active

print(list_devices)
for i in range(len(list_devices)):
    ws.cell(row=i+1, column=1).value=list_devices[i]
wb.save("devices.xlsx")

print("Excel file created successfully.")