import concurrent.futures
import time

threads = []
start = time.perf_counter()


def do_something(second):
    print(f"Sleeping for {second} second(s) ...")
    time.sleep(second)
    return f"Done Sleeping after {second} second(s)"


seconds_list = [5, 4, 3, 2, 1]

with concurrent.futures.ThreadPoolExecutor() as executor:

    # this works just like the map function but returns an iterator of function return statement
    # this creates a thread for each element of the seconds_list and returns iterator of function return statement
    # you can't use as_completed method on map iterator because it's type is not future objects
    # as we can see without using as_completed method (which in this case we can't) the first thread that starts is also the first one to finish (the threads finish in order they started)
    results = executor.map(do_something, seconds_list)

    for result in results:
        print(result)


finish = time.perf_counter()

print(f"program finished in {finish - start} seconds")
