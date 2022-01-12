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
    results = [executor.submit(do_something, sec) for sec in seconds_list]

    # as_completed() method takes a sequence of future objects and returns an iterator of those future objects as they are completed(generates each one afters it's completed)
    # as we can see it start the threads from 5 to 1 based on their position in seconds_list but we see that with use of as_completed method we see them finish from 1 to 5 beacuse as soon as a thread is finished this iterator generates it
    for f in concurrent.futures.as_completed(results):
        print(f.result())


finish = time.perf_counter()

print(f"program finished in {finish - start} seconds")
