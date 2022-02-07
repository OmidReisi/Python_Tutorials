import asyncio


async def main():
    print("Omid")

    # here we're awaiting our coroutine's execution.
    await task("text")
    print("finished")


async def task(text):
    print(text)

    # the await keyword is how we execute the coroutines and can't run coroutines without it.
    # the await keyword can only be used in another coroutine (function defined as async).
    # asyncio.sleep() works just like time.sleep() but returns a coroutine instead of None.
    await asyncio.sleep(1)


asyncio.run(main())
