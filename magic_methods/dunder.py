"""
Dunder methods are called dunder because they have double underscores before and after their name.
They are also called magic methods because they allow you to define how your objects behave with built-in functions and operators. 
for example, the __str__ method allows you to define how your object is represented as a string, and the __add__ method allows you to define how your object behaves when added to another object.
"""
(5).__add__(2) // 7

"""
.__init__ is also a dunder method that python calls internally when you create an instance of a class 
"""
class Point:
    def __init__(self,x,y):
        self.x=x;
        self.y=-y;

point = Point(2,3)
print(point.x) # 2
print(point.y) # 3

"""
When you call a constructor to create a new object, python implicitly call the .__new__() method 
and it return a new empty object and then it passes the new object to the .__init__() method to initialize it.
"""

class Storage(float):
    def __new__(cls, value,unit):
        instance = super().__new__(cls, value)
        instance.unit = unit
        return instance

"""
There are mainly two different methods to represent an object as a string 
one needs to be technical and the other needs to be user friendly.
For user friendly representation, python uses the __str__() method and
when you need developer friendly output, python uses the __repr__()
"""
"""
When you call the str() function on an object, python calls the __str__() method
also when you call print() function on an object, python also calls the __str__() method
"""
class Person:
    def __init__(self, name, age):
        self.name=name
        self.age=age

    def __str__(self):
        return f"{self.name} is {self.age} years old"

