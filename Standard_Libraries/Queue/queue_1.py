import queue

# the queue module is mostly used when multiple threads are sharing resources.
# by default the queues are blocking and their timeout is None.

# the queue module has the following classes:
# Queue : FIFO queue
# LifoQueue : FILO queue (stack)
# PriorityQueue : sorts the values in ascending order and it's put method returns the least value.


# the put and get method have the O(1) complexity except the PriorityQueue's put method that has logarithmic complexity.
# PriorityQueue uses Min Heap Queue algorithm to sort values in ascending order and thats why it's put method has logarithmic complexity.


# the following methods and attributes are all available for all queue classes.


# maxsize is an optional parameter that shows the maximum size of the queue.(it's default is 0)
fifo_q = queue.Queue(maxsize=10)

# returns the maxsize of the initialization of the queue.
print(fifo_q.maxsize)

# puts an element in the queue based on the type of the queue.
# if the block is set to False and the queue is full an queue.Full exception is raised.
fifo_q.put(5)

# returns the current size of the queue.
print(fifo_q.qsize())

# returns an element in the queue based on the type of the queue.
# if the block is set to False and queue is empty an queue.Empty exception is raised.
print(fifo_q.get())

# true if the queue is empty
print(fifo_q.empty())

# true if the queue is full
print(fifo_q.full())
