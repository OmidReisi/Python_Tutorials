import threading

# I/O BOUND PROGRAMS: programs that don't use a lot of cpu and don't have much computing and mostly they're spending their time in I/O situations (like file reading and writing, downloading, printing, networking and ...)
# CPU BOUND PROGRAMS: programs that spend most of their time using cpu and computing stuff

# running Concurrently means that we switch back and forth to run different thereds(threading module)
# running Parallel means that we run each thread on different cpu cores if there are multiple cores (multiprocessing module)

# thereding is only good for I/O BOUND programs and might even slow down CPU BOUND programs (for CPU BOUND programs we use multiprocessing module)

# using threading module is also called Concurrent Programming

import time


start = time.perf_counter()


def do_something():
    print("Sleeping for 1 second...")
    time.sleep(1)
    print("Done Sleeping ...")


# to use threading on our functions, we need to create threads for as many times that we want to run that function and pass that funcion as the target of the thread
# always use keyword arguments for Thread
t1 = threading.Thread(target=do_something)
t2 = threading.Thread(target=do_something)

# this method starts the thread (and runs the function on that thread)
t1.start()
t2.start()

# this method terminates the thread (joins the thread to the main thread of the program)
# we terminate the threads here because if we don't then the threads will continue to run the whole program and they print the statement below before the end of time.sleep() in our funcions and our elapsed time won't be correct
t1.join()
t2.join()


finish = time.perf_counter()

# we see here that by using threading it takes less than 2 seconds (around 1 seconds) to finish the program
# this elapsed time still remains 1 seconds if we run the funcion 10 times by using threading
print(f"program finished in {finish - start} seconds")
