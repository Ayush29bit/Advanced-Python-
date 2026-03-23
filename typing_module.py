"""
The typing module provides support for type hints in Python.
It allows developers to specify the expected types of variables, function parameters, and return values, which can help improve code readability and catch potential type-related errors during development.
The module includes various classes and functions for defining complex types, such as lists, dictionaries, and custom classes, as well as tools for creating generic types and type aliases.
By using the typing module, developers can enhance the maintainability and robustness of their code by making type expectations explicit.
""" 
from typing import TypedDict
class Person(TypedDict):
    name:str
    age:int
    email:str

def print_people(people:list[Person]):
    for person in people:
        print(f"Name: {person['name']}, Age: {person['age']}, Email: {person['email']}")

print_people([
    {"name": "Alice", "age": 30, "email": "alice@example.com"}
     ])
     
"""
In this example, we define a TypedDict called Person, which specifies that each person should have a name (string), age (integer), and email (string).
The print_people function takes a list of Person objects and prints their details.
By using the typing module, we can ensure that the data passed to the function is valid according to the expected structure, making our code more robust and easier to understand.
"""

"""Key features:
supports type hints for variables, function parameters,
and return values and classes.
We can customise our own types using Typedvar and newtype
Complex types like list, dict, tuple, and set can be defined using the typing module.

"""

# NamedTuple

from typing import NamedTuple
class User(NamedTuple):
    id: int
    name: str
    email: str

def greet_user(user: User):
    print(f"Hello, {user.name}! Your email is {user.email}.")

greet_user(User(id=1, name="Alice", email="alice@example.com"))

"""
In this example, we define a NamedTuple called User,
 which has three fields: id (integer), name (string), and email (string).
"""

#TypedDict
from typing import TypedDict

class Product(TypedDict):
    id: int
    name: str
    price: float

def print_product(product: Product):
    print(f"Product ID: {product['id']}, Name: {product['name']}, Price: ${product['price']}")

"""
In this example, we define a TypedDict called Product,
which specifies that each product should have an id (integer), name (string), and price (float).
The print_product function takes a Product object and prints its details.
The typing module allows us to ensure that the data passed to the function is valid according to the expected structure, making our code more robust and easier to understand.
"""

# TypedVar

from typing import TypedVar
T = TypedVar("T")

def identity(value: T) -> T:
    return value

from typing import Dict, Union

UserData = Dict[str, Union[str, int]]

def format_user(user: UserData) -> str:
   
   return f"{user['name']} is {user['age']} years old"

format_user({"name": "Charlie", "age": 40})

#CALLABLE 

"""
Example : An order processing system where you want to apply discounts to products
"""

from typing import Callable, NewType

OrderID = NewType('OrderID', int)
def apply_discount(price: float, discount_func: Callable[[float], float]) -> float:
    return discount_func(price)

def process_order(order_id: OrderID, price: float, discount_func: Callable[[float], float]) -> str:
    return apply_discount(price, discount_func)

"""
This example shows how to use NewType
to create a type for order IDs and Callable to define a flexible function signature for discounts.
"""

# Protocols 

from typing import Protocol

class Greeter(Protocol):
    def greet(self) -> str:
        ...

class FriendlyGreeter:
    def greet(self) -> str:
        return "Hello! Friend"
    
def welcome(greeter: Greeter) -> str:
    return greeter.greet()

welcome = FriendlyGreeter()
print(welcome(welcome))

"""

"""

