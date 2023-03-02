'''Write a Python program to read each row from a given csv file and print a list of strings.'''
import csv

with open("new.csv","r") as cs:
	reader = csv.reader(cs)
	for row in reader:
		print(",".join(row))
