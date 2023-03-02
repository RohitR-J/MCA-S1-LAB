"""Write a Python program to read specific columns of a given CSV file and print the content
of the columns."""
import csv
with open("new.csv","r") as cs:
	read = csv.reader(cs)
	n = int(input("Enter index"))
	for rows in read:
		
		print(rows[n])
		
