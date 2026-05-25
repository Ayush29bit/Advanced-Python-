"""
*args and **kwargs are used in function definitions to allow for variable numbers of arguments.
*args allows a function to accept any number of positional arguments.
**kwargs allows a function to accept any number of keyword arguments.

keyword arguments are passed to a function using the syntax key=value, and they are collected into a dictionary when using **kwargs.
positional arguments are passed to a function without any specific syntax, and they are collected into a tuple when using *args.
"""
def tea_order(customer_name, tea_type):
    print(customer_name, "ordered a cup of", tea_type)

tea_order("Alice", "Green Tea") # This will print: Alice ordered a cup of Green Tea
tea_order("Bob", "Black Tea", "oat") # This will raise a TypeError, as the function only accepts two positional arguments.

"""
With the help of *args
"""
def tea_order(customer_name,tea_type,*args):
    print(customer_name, "ordered a cup of", tea_type, "and")

"""
The *args tells python whatever number of variables are 
coming should be stored in a tuple
"""
def tea_order(customer_name,tea_type,*args):
    print(customer_name, "ordered a cup of", tea_type, "and")
    print("args contains", args)
    for arg in args:
        print("Add:",arg)

tea_order("Ayush","CHAI","hONEY","MAGGIE")


"""
**kwargs tell python to take n number of keyword arguments
and pack them into a dictionary 
{}
"""

def tea_order(customer_name,tea_type,**kwargs):
    print(customer_name, "ordered a cup of", tea_type, "and")
    print("kwargs contains", kwargs)
    for kwarg in kwargs:
        print("Add:",kwarg)

tea_order("Ayush","CHAI",milk="Almond")
