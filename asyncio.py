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