# Code for part 1: Script 2
try:
    file = pd.read_csv(filename)
except:
    try:
        file = json.load(filename)
        file = pd.DataFrame(file)
    except:
        print('Could not open this file')

datatoexcel = pd.ExcelWriter('exported_data.xlsx')

# write DataFrame to excel
file.to_excel(datatoexcel)

# save the excel
datatoexcel.save()
print('The Data has been written to an Excel File successfully.\n'
      'The file is named "exported_data.xlxs"\n'
      'The Data has', file.shape[1], 'columns and', file.shape[0], 'rows')

