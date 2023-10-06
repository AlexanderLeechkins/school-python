class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def get_area(self):
        return self.width * self.height
    def get_perimeter(self):
        return 2 * (self.width + self.height)
    def get_diagonal(self):
        return round((self.width ** 2 + self.height ** 2) ** 0.5)
        
rectangle1= Rectangle(7,8)
print(rectangle1.get_area())
print(rectangle1.get_perimeter())
print(rectangle1.get_diagonal())

rectangle2= Rectangle(12,5)
print(rectangle2.get_area())
print(rectangle2.get_perimeter())
print(rectangle2.get_diagonal())

rectangle3= Rectangle(3,4)
print(rectangle3.get_area())
print(rectangle3.get_perimeter())
print(rectangle3.get_diagonal())

if rectangle1.get_area() == 56:
    print ("true")
if rectangle1.get_perimeter() == 30:
    print("true")
if rectangle1.get_diagonal() == 11:
    print ("true")

if rectangle2.get_area() ==60 :
    print ("true")
if rectangle2.get_perimeter() == 34:
    print("true")
if rectangle2.get_diagonal() == 13:
    print ("true")

if rectangle3.get_area() == 12:
    print ("true")
if rectangle3.get_perimeter() == 14:
    print("true")
if rectangle3.get_diagonal() == 5:
    print ("true")




