import openpyxl

# Create a new Excel workbook object
new_Excel_File = openpyxl.Workbook()

# Save the newly created workbook with a specified filename (you need to provide the filename)
new_Excel_File.save("new_workbook.xlsx") 