import time


start = time.perf_counter()


def do_something():
    print("Sleeping 1 second ...")
    time.sleep(1)
    print("Done Sleeping ...")


do_something()
do_something()

finish = time.perf_counter()

print("script executed in {} seconds".format(round(finish - start, 5)))


# as we can see this program is just waiting(sleeping) for 1 second and with thereding we can continue with the program while it is sleeping
