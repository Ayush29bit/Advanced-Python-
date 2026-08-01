import sys

a = [1, 2, 3]
print(sys.getrefcount(a))  # Output: 2

"""
Reference Counting in Python
Reference counting is a memory management technique used in Python to keep track of the number of references to an object.
Each time a new reference to an object is created, the reference count is incremented, and when a reference is deleted or goes out of scope,
the reference count is decremented. When the reference count reaches zero, the memory occupied by the object can be safely deallocated.

"""
"""
Why is the output 2 and not 1?

When we pass the variable a into sys.getrefcount(a), the function itself creates a temporary reference to the object inside its execution scope. 
Therefore, the total count is:
The global variable a pointing to the list.
The internal argument placeholder inside sys.getrefcount() pointing to the list.
"""

b = a  # Create a new reference
print(sys.getrefcount(a))  # Output: 3 (a, b, and the function argument)

c = [a, a]  # Put it inside a list twice
print(sys.getrefcount(a))  # Output: 5 (a, b, two slots in c, and the function)

del b  # Remove one reference
print(sys.getrefcount(a))  # Output: 4
