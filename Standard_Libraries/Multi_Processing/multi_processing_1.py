# I/O BOUND PROGRAMS: programs that don't use a lot of cpu and don't have much computing and mostly they're spending their time in I/O situations (like file reading and writing, downloading, printing, networking and ...)
# CPU BOUND PROGRAMS: programs that spend most of their time using cpu and computing stuff

# running Concurrently means that we switch back and forth to run different thereds(threading module)
# running Parallel means that we run each thread on different cpu cores if there are multiple cores (multiprocessing module)

# multiprocessing is good for both CPU BOUND and I/O BOUND PROGRAMS.

# using multiprocessing module is also called Parallel Programming

import multiprocessing
import time


def do_something():
    print("Sleeping 1 second ...")
    time.sleep(1)
    print("Done Sleeping ...")


# for multiprocessing module we should always make sure that the module is being run directly and can safly be imported so we use if __name__ == "__main__":
if __name__ == "__main__":

    start = time.perf_counter()

    # the syntax for multiprocessing module is just like Threading and we just use Process class instead of Thread class
    p1 = multiprocessing.Process(target=do_something)
    p2 = multiprocessing.Process(target=do_something)

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    finish = time.perf_counter()

    print(f"program finished in {finish - start} seconds.")
