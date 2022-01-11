import sys

# bothe work like print() function but they don't add \n automatically(use the first one for outputing errors only)
sys.stderr.write("This is an error text.\n")
sys.stdout.write("This is a normal text.")
