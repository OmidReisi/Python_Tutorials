# just like ThreadPoolExecutor we have ProcessPoolExecutor for multiprocessing and it's syntax is just like ThreadPoolExecutor

import concurrent.futures
import time


def do_something(second):
    print(f"Sleeping {second} second(s)...")
    time.sleep(second)
    return "Done Sleeping ..."


if __name__ == "__main__":

    start = time.perf_counter()

    with concurrent.futures.ProcessPoolExecutor() as executor:
        f1 = executor.submit(do_something, 1.5)
        f2 = executor.submit(do_something, 1.5)
        print(f1.result())
        print(f2.result())

    finish = time.perf_counter()

    print(f"program finished in {finish - start} seconds.")
