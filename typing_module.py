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
