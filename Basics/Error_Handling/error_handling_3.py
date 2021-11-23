try:
    name = "corrupt_file"
    if name == "corrupt_file":
        # we can raise our own exceptions this way
        raise Exception
except Exception:
    print("Error!")
