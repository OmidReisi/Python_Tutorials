import time

# all the following method should be used as intervals (finish - start) and their single value is meaningless
# perf_counter functions (both seconds and nanoseconds) are more precise and calculate time.sleep() time between them as well
# process_time functions (both seconds and nanoseconds) only calculate cpu usage time and ignore time.sleep() and memory usage time
# if you want to see the program time perf_counter is the best method and don't ever use time.time() for performance measurements


# this returns a float of the process time in seconds
start = time.perf_counter()
a = 10
finish = time.perf_counter()
print(finish - start)

# this returns an integer of the process time in nanoseconds
start = time.perf_counter_ns()
a = 10
finish = time.perf_counter_ns()
print(finish - start)


start = time.process_time()
a = 10
finish = time.process_time()
print(finish - start)


start = time.process_time_ns()
a = 10
finish = time.process_time_ns()
print(finish - start)
