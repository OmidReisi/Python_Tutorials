import asyncio


async def fetch_data():
    print("start fetching")
    await asyncio.sleep(2)
    print("done fetching")
    return {"data": 1}


async def print_numbers():
    for i in range(10):
        print(i)
        await asyncio.sleep(0.25)


async def main():
    task1 = asyncio.create_task(fetch_data())
    task2 = asyncio.create_task(print_numbers())

    # in order to make sure that tasks finish we need to await them like coroutines.
    # the main function doesn't move forward untill task1 is finished.
    # we can get the return from a task only after it's finished.
    # while a task is not finished it's return object is called a future object.
    # a future object is something that doesn't exist right now but it's going to be available in the future.
    value = await task1
    print(value)
    print("task1 is finished.")

    # as we can see task2 doesn't finish because we've not awaited it.

    await task2

    print("task2 is finished.")


asyncio.run(main())
