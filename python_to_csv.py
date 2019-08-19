import json
import csv

#making columns for csv files
csv_columns = ['interface','mac']
#Taking input from json file and converting it into dictionary data format

with open('mac_address_table_sw1','r') as read_mac_sw1:
    fout = json.loads(read_mac_sw1.read())
print(fout)

#naming a csv file
csv_file = 'names.csv'
try:
    with open(csv_file,'w') as csvfile:
        #DictWriter function creates an object and maps dictionary onto output rows.
        # fieldnames fieldnames parameter is a sequence of keys that identify the
        # order in which values in the dictionary passed to the writerow() method are written to file "csv_file"

        # extrasaction : If the dictionary passed to the writerow() method contains a key not found in fieldnames,
        # the optional extrasaction parameter indicates what action to take. If it is set to 'raise', the default
        # value, a ValueError is raised. If it is set to 'ignore', extra values in the dictionary are ignored.
        writer = csv.DictWriter(csvfile, fieldnames=csv_columns, extrasaction='ignore')
        writer.writeheader()
        for data in fout:
            writer.writerow(data)
except IOError:
    print('I/O error')