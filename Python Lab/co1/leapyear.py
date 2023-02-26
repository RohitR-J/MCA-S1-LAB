current = int(input("Enter current year:"))
final = int(input("Enter final year:"))

for leap in range(current,final+1):
    if(leap%400 == 0 and leap%100 == 0):
        print(leap)
    elif(leap%4 == 0 and leap%100 != 0):
        print(leap)

