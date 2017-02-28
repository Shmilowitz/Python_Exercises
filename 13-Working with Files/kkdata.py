import csv
import pprint
import openpyxl

# OrderedDict
f = open("befkbhalderstatkode.csv", 'rt')
try:
    reader = csv.DictReader(f)
    for row in reader:
        print(row)
finally:
    f.close()
	
# Print every row
# pp = pprint.PrettyPrinter(indent=4)
# reader = csv.reader(open("befkbhalderstatkode.csv"))
# STATISTICS={}
# for row in reader:
	# pp.pprint(row)
	# STATISTICS[row[0]] = row[1:]



#Didnot work
# with open('befkbhalderstatkode.csv') as f:
    # _ = next(f)
    # reader = csv.DictReader(f)
# for line in reader: 
	# STATISTICS[row[0]] = dict(zip(headers, row[1:]))
	# STATISTICS[row[0]]['Stabling'] = [s.strip() for s in STATISTICS[row[0]]['Stabling'].split(',')]
	
wb = openpyxl.load_workbook('iris_data.xlsx')
print(wb.get_sheet_names())
sh = wb.get_active_sheet()
print(sh)
with open('test.csv', 'w') as f:
    c = csv.writer(f)
    for r in sh.rows:
        c.writerow([cell.value for cell in r])