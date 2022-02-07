# we can use asynch requests with requests-html without any external modules.

import time

# we use AsyncHTMLSession for async requests
from requests_html import AsyncHTMLSession


session = AsyncHTMLSession()

t1 = time.perf_counter()


# async def get_delay1():
#     response = await session.get(r"https://httpbin.org/delay/1")
#     return response


# async def get_delay2():
#     response = await session.get(r"https://httpbin.org/delay/2")
#     return response


# async def get_delay3():
#     response = await session.get(r"https://httpbin.org/delay/3")
#     return response


async def get_delay(url):
    response = await session.get(url)
    return response


t1 = time.perf_counter()

# the session.run method only works on coroutine funcions, not coroutines themselves, which means your coroutines can't accept any input.
# either use asyncio for coroutines with inputs or use lambda to pass your arguments but still pass a callable to the session.run() method

# this is the first way with different coroutine functions with no arguments
# results = session.run(get_delay1, get_delay2, get_delay3)

# this is the second way by using lambda by passing callables to session.run()
results = session.run(
    lambda: get_delay("https://httpbin.org/delay/1"),
    lambda: get_delay("https://httpbin.org/delay/2"),
    lambda: get_delay("https://httpbin.org/delay/3"),
)

for result in results:
    r = result.html.url
    print(r)


t2 = time.perf_counter()

print(f"Asynchronous: {t2-t1} seconds")
