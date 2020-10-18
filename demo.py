import csv
with open('demo_list.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)