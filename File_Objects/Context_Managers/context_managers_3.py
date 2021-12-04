import os
from contextlib import contextmanager


@contextmanager
def change_dir(destination_path):
    try:
        cwd = os.getcwd()
        os.chdir(destination_path)
        # if we're not working with any objects in our context manager then we yield nothing (but we have to write down the yield statement itself)
        yield
    finally:
        os.chdir(cwd)


with change_dir(r"../"):
    print(os.listdir())

print(os.listdir())
