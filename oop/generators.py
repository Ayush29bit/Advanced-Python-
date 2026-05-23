"""
Generators are special functions that allow you to create iterators in a more memory-efficient way.
They use the `yield` keyword to produce a sequence of values, one at a time, instead of returning them all at once.
This can be particularly useful when working with large datasets or infinite sequences, as it allows you to generate values on-the-fly without consuming a lot of memory.
"""
def gen_values():
    yield 1 
    yield 2 
    yield 3 

gen_values_object=gen_values() # This will return a generator object, not the values themselves.

next(gen_values_object) # This will return 1, the first value yielded by the generator.
next(gen_values_object) # This will return 2, the second value yielded by the generator.
next(gen_values_object) # This will return 3, the third value yielded by the generator 
next(gen_values_object) # This will raise a StopIteration exception, as there are no more values to yield.

for values in gen_values_object():
    print(values) # This will print the values yielded by the generator, one at a time.

def get_primes_list(start,end):
    primes = []
    for num in range(start, end+1):
        if num < 2 :
            continue
        is_prime = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return primes

"""
Basically, A generator is a special type of iterator that produces values one at a time instead of storing everything in memory at once.
"""

"""
Example of memeory efficiency of generators:
"""
# List Comprehension
squares = [x*x for x in range(1000000)]

"""
This creates the ENTIRE list immediately in memory.
"""

# Generator Expression
squares_gen = (x*x for x in range(1000000))

"""
This creates a generator that produces squares one at a time, which is much more memory efficient.
"""