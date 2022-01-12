import threading
import time

threads = []
start = time.perf_counter()


def do_something(second):
    print(f"Sleeping for {second} second(s) ...")
    time.sleep(second)
    print("Done Sleeping ...")


# this is how we create multiple threads in a for loop
# underscore (_) means a variable that we don't want to use
# in order to pass arguments for our funcions we should pass them in a iterable (it's best to pass them as a tuple) as args keyword argument
for _ in range(10):
    t = threading.Thread(target=do_something, args=(3.6))
    t.start()
    threads.append(t)

for thread in threads:
    thread.join()


finish = time.perf_counter()

print(f"program finished in {finish - start} seconds")
