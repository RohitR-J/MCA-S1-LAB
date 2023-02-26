#Accept a file name from user and print extension of that. 

filename = input("Enter filename")
extension = filename.split(".")
print(f"The file extension is '{extension[-1]}' ")
