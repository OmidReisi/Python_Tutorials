import asyncio


async def factorial(name, number):
    f = 1
    for i in range(2, number + 1):
        print(f"Task {name}: Compute factorial({number}), currently i={i}...")
        await asyncio.sleep(1)
        f *= i
    print(f"Task {name}: factorial({number}) = {f}")
    return f


async def main():

    # this is one way of creating multiple tasks and running them asynchronously
    # task1 = asyncio.create_task(factorial("A", 2))
    # task2 = asyncio.create_task(factorial("B", 3))
    # task3 = asyncio.create_task(factorial("C", 4))
    # await task1
    # await task2
    # await task3

    # this is another way of doing it. both way do the exact same thing
    # gather method takes coroutines and warps them in tasks and runs them asynchronously
    # the return statement of each coroutine is stored in a list with the order they were passed to the gather method.
    L = await asyncio.gather(
        factorial("A", 2),
        factorial("B", 3),
        factorial("C", 4),
    )
    print(L)


# you can use these 3 lines to create a event loop manually and running your main coroutine.
# it is always recommended to use asyncio.run() instead of these lines unless you want to control the loop for low level purposes.(like creating frameworks)
# remember to always close the event loop (two events loops can't coexist at the same time.)
# remember that you can't use context managers with event loops.
event_loop = asyncio.get_event_loop()
event_loop.run_until_complete(main())
event_loop.close()
print(event_loop.is_closed())
