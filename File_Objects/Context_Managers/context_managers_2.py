# this module is used for creating context managers with functions instead of classes
from contextlib import contextmanager


# everything before yield is like __enter__ method
# everything after yield is like __exit__ method
@contextmanager
def open_file(file, mode):
    try:
        f = open(file, mode)
        yield f
    finally:
        f.close()


with open_file(r"./sample.txt", "w") as f:
    f.write("Lorem ipsum dolor sit amet, consectetur adipiscing elit.")

print(f.closed)
