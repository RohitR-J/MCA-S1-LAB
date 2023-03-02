'''
Create Rectangle class with attributes length and breadth and methods to find area and
perimeter. Compare two Rectangle objects by their area. 
'''
class Rectangle:
    def __init__(self,length,breadth):
        self.length = length
        self.breadth = breadth
    
    def area(self):
        return self.length * self.breadth
    def perimeter(self):
        return 2*(self.length + self.breadth)

length1 = int(input("Enter length of rect1:"))
breadth1 = int(input("Enter breadth of rect1:"))
length2 = int(input("Enter length of rect2:"))
breadth2 = int(input("Enter breadth of rect2:"))

rect1 = Rectangle(length1, breadth1)
rect2 = Rectangle(length2, breadth2)

print("Rectangle1 Area = ",rect1.area()," Perimeter = ",rect1.perimeter())
print("Rectangle2 Area = ",rect2.area()," Perimeter = ",rect2.perimeter())

if rect1.area() > rect2.area():
    print("Area of rect1 is greater")
elif rect1.area() == rect2.area():
    print("Area of rect1 and rect2 are equal")
else:
    print("Area of rect2 is greater")

