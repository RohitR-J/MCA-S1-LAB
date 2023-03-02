'''Write a Python program to write a Python dictionary to a csv file. After writing the CSV file
read the CSV file and display the content.'''

import csv

filename = 'new.csv'
data = {"Name":"Rohit","Age":12}
with open(filename,'w') as cs:
	writer = csv.DictWriter(cs,fieldnames = data.keys())
	writer.writeheader()
	writer.writerow(data)
	
with open(filename,"r") as cs:
	reader = csv.DictReader(cs)
	for rows in reader:
		print(rows)
