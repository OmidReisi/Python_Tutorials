try:
    var = "okay"
except Exception as error:
    print(error)

# if no exception rises in try block the else block runs
else:
    print("All is good no Error")

# finally block executes no matter what
finally:
    print("Error or no Error this block executes")
