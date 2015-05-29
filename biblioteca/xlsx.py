import xlsxwriter

workbook = xlsxwriter.Workbook('hello.xlsx')
worksheet = workbook.add_worksheet()

worksheet.write('A1', 'Hello world')

workbook.close()

# Create a Pandas dataframe from the data.
df = pd.DataFrame([10, 20, 30, 20, 15, 30, 45])
# Create a Pandas Excel writer using XlsxWriter as the engine.
writer = pd.ExcelWriter('simple.xlsx', engine='xlsxwriter')
df.to_excel(writer, sheet_name='Sheet1')

# Close the Pandas Excel writer and output the Excel file.
writer.save()
