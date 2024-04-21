# Operations From Python to Excel File

This repository was created using the Python language to 'extract data' from an Excel file, 'read data', and 'create the Excel file'.

## File Contents

Note: There will be a general statement that you can see in these files.

```python
excel_File = openpyxl.load_workbook("")
page = excel_File[""]
```
We have provided sample filenames to run on sample files, but you can provide your own filenames and page names to run on your own files and find the page you want to work on.

## Code Explanations

I tried to explain the codes with explanation lines and I would like to talk about some of the tricks I experienced:

1. When applying 'openpyxl.load_workbook("")', if the Excel file is in the same location, you only need to write its name and extension; If it is in different locations, it would be correct to write the direct location. Otherwise, the file will not work.

2. 'max_row' and 'max_column' methods are useful for obtaining maximum column and row information for the loop while reading.

3. The 'save("")' method should be applied last, especially during printing and rendering operations.

## Acknowledgment

Finally, I would like to thank AI for the explanation lines. I am open to criticism, please criticize me. Thanks.
