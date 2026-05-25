from pydantic import BaseModel,field_validator,model_validator,computed_field  #type:ignore

class User(BaseModel):
    username:str

    @field_validator("username")
    def username_length(cls,v):
        if len(v)<4:
            raise ValueError("Username must be at least 4 characters long")
        return v
    
"""
Field validators are used to validate individual fields in a Pydantic model.
In this example, we have a User model with a username field. The @field_validator decorator is used to define a validation function for the username field. The function checks if the length of the username is at least 4 characters long, 
and if not, it raises a ValueError.
"""

"""
Model validators are used to validate the entire model after all fields have been validated.
field_validator - Individual fields
model_validator	- Whole model / multiple fields together
"""

class Signup(BaseModel):
    password:str
    confirm_password:str

    @model_validator(mode="after")
    def passwords_match(cls,v):
        if v["password"]!=v["confirm_password"]:
            raise ValueError("Passwords do not match")
        return v
    
from datetime import date

class Booking(BaseModel):
    start_date: date
    end_date: date

    @model_validator(mode="after")
    def validate_dates(self):
        if self.end_date <= self.start_date:
            raise ValueError("End date must be after start date")

        return self
    
class Product(BaseModel):
    price:float 
    quantity:int

    @computed_field
    @property 
    def total_cost(self):
        return self.price * self.quantity
    

class Booking(BaseModel):
    user_id:int
    room_id:int
    nights:int
    rate_per_night:float 
    

    @field_validator("nights")
    def nights_validate(cls,v):
        if v <=1:
            raise ValueError("nights grater than 1")
        return v 
    
    @computed_field
    @property
    def total_amount(self):
        self.total_amount=self.nights*self.rate_per_night

      
    