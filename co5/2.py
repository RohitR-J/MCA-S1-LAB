'''Python program to copy odd lines of one file to other'''

with open("new.txt","r") as inpfile:
	linenum = 1
	with open("new1.txt","w") as outfile:
		for  line in inpfile:
			if linenum %2 != 0:
				outfile.write(line)
			linenum+=1
with open("new1.txt","r") as outfile:
	print(outfile.read())

