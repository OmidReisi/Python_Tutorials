import multiprocessing
import time


def do_something(second):
    print(f"Sleeping {second} second(s)...")
    time.sleep(second)
    print("Done Sleeping ...")


if __name__ == "__main__":

    process_list = []

    start = time.perf_counter()

    for _ in range(10):
        p = multiprocessing.Process(target=do_something, args=(2.5,))
        p.start()
        process_list.append(p)

    for process in process_list:
        process.join()

    finish = time.perf_counter()

    print(f"program finished in {finish - start} seconds.")
