"""
This code demonstrates a cyclic reference. 
A cyclic reference occurs when two or more objects reference each other, creating a cycle that can prevent the garbage collector from reclaiming memory.

"""

class Person:
    pass

alice = Person()
bob = Person()

alice.friend = bob
bob.friend = alice  # Create a cyclic reference

"""
```
alice ------------> Person A
                     |
                     |
                     ▼
                  Person B <------ bob
```
"""

"""
```
             +----------------+
             |                |
             ▼                |
alice ---> Person A --------> Person B <--- bob
             ^                |
             |                |
             +----------------+

```
Now reference counts for both Person A and Person B are 2, as they reference each other.
Person A = 2
Person B = 2

"""

del alice
del bob

"""
After deleting the references to alice and bob, the reference counts for both Person A and Person B are still 1, as they reference each other.

Person A and B know each other but nobody else knows them. So they are not reachable from the outside world, but they are still alive because they reference each other.
They are occupying memory but are not accessible, leading to a memory leak.
"""

