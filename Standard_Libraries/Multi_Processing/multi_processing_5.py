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
        results = executor.map(do_something, secs)

        for result in results:
            print(result)

    finish = time.perf_counter()

    print(f"program finished in {finish - start} seconds.")
