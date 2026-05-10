"""
The asyncio library allows us to write concurret code 
using aync and await keywords.

Core building blocls of aync IO are the awaitable objects(coroutines)
that are scheduled and executed by an event loop
"""

#   Without Asyncio 

import time

def task():
    time.sleep(2)  # simulating I/O wait
    print("Done")

task()
task()

"""
Total time ≈ 4 second
Blocking
"""
# with asyncio 

import asyncio

async def task():
    await asyncio.sleep(2)
    print("Done")

async def main():
    await asyncio.gather(task(), task())

asyncio.run(main())

"""
Total time ≈ 2 seconds
Both tasks run concurrently (not parallel, but overlapping)
"""

"""
Related terms 

Parallelism : executing multiple operations at the same time
Multiprocessing : way of acheiving parallelism by spreading tasks over a computer's CPU
Concurrency : Multiple tasks having the ability to run in overlapping manner
Threading : Concurrent execution model in which multiple threads take turns executing tasks
"""
"""
Concurrency is a concept and asyncio is a technique to implement it 
Parallelism is a concept and multoprocessing is a technique to implement it 
"""

"""
The asyncio package is billed by the Python documentation as a library to write concurrent code.
However, async I/O isn’t threading or multiprocessing. It’s not built on top of either of these.
Async I/O is a single-threaded, single-process technique that uses cooperative multitasking. 
Async I/O gives a feeling of concurrency despite using a single thread in a single process.

"""

"""
What does it mean to be Asynchronous?
Asynchronous routines can pause their execution while waiting for a result and allow other routines to run in the meantime.
Asynchronous code facilitates the concurrent execution of tasks by coordinating asynchronous routines.
"""

"""
Async and Await and Coroutines

The async def syntax construct introduces either a coroutine function or an asynchronous generator.
The await keyword suspends the execution of the surrounding coroutine and passes control back to the event loop.
"""


""" 
async def g():
    result = await f()  # Pause and come back to g() when f() returns
    return result
    
"""