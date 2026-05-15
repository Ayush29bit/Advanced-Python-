"""
Pydantic is a data validation and settings management library for Python. 
It allows you to define data models using Python classes, and it provides powerful features for validating and parsing data.
Pydantic is often used in web development, data processing, and any situation where you need to ensure that the data you're working with adheres to a specific structure.
"""
from pydantic import BaseModel #type:ignore

class Product(BaseModel):
    id:int
    name:str
    price:float
    in_stock:bool=True

"""
Pydantic uses type annotations to define the fields of the model.
In this example, we have a Product model with four fields: id, name, price, and in_stock. The in_stock field has a default value of True.
"""
from pydantic import BaseModel, Field #type:ignore
from typing import typing, List, Dict, Optional

class Cart(BaseModel):
    user_id:int
    items:List[str]
    quantities:Dict[str,int]

class BlogPost(BaseModel):
    title:str
    content:str
    image_url:Optional[str]=None

"""
Pydnatic also supports more complex data types, such as lists and dictionaries.
In the Cart model, we have a list of items and a dictionary that maps item names to their quantities.
The BlogPost model includes an optional field for an image URL, which can be None if not provided."""

class Employee(BaseModel):
    id:int 
    name:str=Field(..., min_length=3) # The ... indicates that this field is required, and min_length=1 ensures that the name cannot be an empty string.
    salary:float=Field(...,ge=10000)
    department:Optional[str]


