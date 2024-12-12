class Rectangle:
    def __init__( self, length, breadth ):
        self._length=length
        self._breadth=breadth

    def area(self):
        return self._length * self._breadth

    def __lt__(self, other):
        return self.area() < other.area()

print("RECTANGLE 1")
length1=int(input("enter the length of Rectangle 1:"))
breadth1=int(input("enter the breadth of a Rectangle 1:"))
rect1=Rectangle(length1,breadth1)
print(f"the area of Rectangle 1 is:{rect1.area()}")
print("\nRECTANGLE 2")
length2=int(input("enter the length of the Rectangle 2:"))
breadth2=int(input("enter the breath of the Rectangle 2:"))

rect2=Rectangle(length2,breadth2)
print(f"the area of Rectangle 2 is:{rect2.area()}")
print("\nnow comparing the Rectangles")
if rect1 < rect2:
    print("the area of the Rectangle 1 is less than rectangle 2. ")
elif rect2 < rect1:
    print("the area of Rectangle 2 is less than rectangle 1. ")
else:
    print("both the Rectangles have the same area.")