# from python 3.2 forward there is the concurrent.futures module which is the new and better way of using threading in python

import concurrent.futures
import time

threads = []
start = time.perf_counter()


def do_something(second):
    print(f"Sleeping for {second} second(s) ...")
    time.sleep(second)
    return "Done Sleeping ..."


# this way of using threading in python requires context managers
# inside the context manager threads are executed and at the end of context manager the threads join each other
with concurrent.futures.ThreadPoolExecutor() as executor:
    # with submit we start the thread for the given function (arguments are passed after the function name as positional arguments)
    # the submit method encapsulates the execution of the function and returns a future object for it
    # with the future object we can see the status of our function (if it's running or is it done or ...)
    # we can also get the return statement of our funcion from the future object
    # in order to get multiple threads we run the submit method multiple times
    f1 = executor.submit(do_something, 2.5)
    f2 = executor.submit(do_something, 2.5)

    # this is how we get the return statement of our funcion from the future object
    # running the result method actually hold the thread untill the function is done(it's like not using threading) so we need to use our result() methods after we've created our threads
    print(f1.result())
    print(f2.result())


finish = time.perf_counter()

print(f"program finished in {finish - start} seconds")
