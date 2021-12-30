import subprocess

# we added a directory that doesn't exist for our command
# note that python doesn't raise an exception for errors in external commands
p1 = subprocess.run(["ls", "-la", "dne"], capture_output=True, text=True)

# now that the command has an error the returncode is no longer 0
print(p1.returncode)

# we can see the error with stderr
# if hadn't set stderr, stdout to subprocess.PIPE then the error would've been printed to the terminal
print(p1.stderr)


# to make python raise an exception if an external error occurs we use the check argument
p2 = subprocess.run(["ls", "-la", "dne"], capture_output=True, text=True, check=True)


# you can ignore external error if you pass the error to subprocess.DEVNULL
p3 = subprocess.run(["ls", "-la", "dne"], stderr=subprocess.DEVNULL)
