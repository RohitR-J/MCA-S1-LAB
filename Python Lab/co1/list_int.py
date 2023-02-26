"""
Enter 2 lists of integers. Check
(a) Whether list are of same length
(b) whether list sums to same value
(c) whether any value occur in both 
"""

lis1 = [1,2,3,4,5,6]
lis2 = [12,23,34,34,34,34]

if len(lis1)==len(lis2):
    print("lengths are same")
else:
    print("lengths are not same")

if sum(lis1)==sum(lis2):
    print("Sums are same")
else:
    print("sums are not same")

intr = set(lis1).intersection(set(lis2))
if intr:
    print("The common elements are",intr)
else:
    print("They dont have any common elements")

