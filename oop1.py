class Rectangle:
    def __init__(self,length,breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

    def perimeter(self):
        return 2 * (self.length + self.breadth)

    def display(self):
        print(f"area of rectangle :{self.area()}")

        print(f"perimeter of rectangle:{self.perimeter()}")

    def compare_area(self,other):
        if self.area() == other.area():
            print(f"Rectangle are equal in area ")
        elif self.area() > other.area():
            print("\nRectanle 1 is greater in area than rectangle 2;")
        else:
            print("\nRectanle 2 is greater in area than rectangle 1; ")


print("enter dimentions of the 1st rectangle")
length1 = int(input("enter length 1"))
breadth1 = int(input("enter breadth 1"))
rect1 = Rectangle(length1, breadth1)

rect1.display()

print("enter dimentions of the 2nd rectangle")
length2 = int(input("enter length 2"))
breadth2 = int(input("enter breadth 2"))
rect2 = Rectangle(length2,breadth2)
rect2.display()

rect2= Rectangle(length2,breadth2)
rect2.display()
rect1.compare_area(rect2)
