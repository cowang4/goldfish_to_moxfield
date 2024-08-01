import csv

with open('my_collection.csv') as inputfile:
    reader = csv.DictReader(inputfile)
    with open('moxfield_collection.csv', '+w') as outputfile:
        fieldnames = ['Count', 'Name', 'Edition', 'Condition', 'Language', 'Foil', 'Collector Number', 'Alter', 'Proxy', 'Purchase Price']
        writer = csv.DictWriter(outputfile, fieldnames=fieldnames)
        writer.writeheader()
        for row in reader:
            print(row)
            out = {}
            out['Count'] = row['Quantity']
            out['Name'] = row['Card']
            out['Edition'] = row['Set ID']
            out['Condition'] = 'NM'
            out['Language'] = 'en'
            out['Foil'] = '' if row['Foil'] == 'regular' else 'foil'
            out['Collector Number'] = row['Collector Number']
            out['Alter'] = 'FALSE'
            out['Proxy'] = 'FALSE'
            out['Purchase Price'] = ''
            print(out)
            writer.writerow(out)