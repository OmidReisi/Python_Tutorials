import concurrent.futures
import time


def do_something(second):
    print(f"Sleeping {second} second(s)...")
    time.sleep(second)
    return f"Done Sleeping for {second} seconds ..."


if __name__ == "__main__":

    start = time.perf_counter()

    with concurrent.futures.ProcessPoolExecutor() as executor:
        secs = [5, 4, 3, 2, 1]
        results = [executor.submit(do_something, sec) for sec in secs]

        for result in concurrent.futures.as_completed(results):
            print(result.result())

    finish = time.perf_counter()

    # as we can see this take 3 seconds instead of around 1.5 seconds and the reason for it is that ProcessPoolExecutor decided to use less processes based on the hardware of our computer
    # because the ProcessPoolExecutor automatically adjusts itself with the hardware of our computer it's better to use it instead of the old fashioned way
    print(f"program finished in {finish - start} seconds.")
