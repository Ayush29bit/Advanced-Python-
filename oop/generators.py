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