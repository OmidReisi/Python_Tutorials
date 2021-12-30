from os import pardir
import subprocess

# if you set standard output to true then it's not printed to terminal
p1 = subprocess.run(["ls", "-la"], capture_output=True)


print(p1.args)

print(p1.returncode)

# no that we're capturing stdout this returns the output and does not return None anymore
# stdout is captured as bytes (b before the text) and puts \n instead of ending lines
print(p1.stdout)

# you can decode bytes to string with decode() method
# the default encoding is "UTF-8"
# as you can see we can use the stdout multiple times when capturing it
print(p1.stdout.decode(encoding="UTF-8"))

print(p1.stdout.decode())


# you can set the text argument to true if you don't want to get bytes on your stdout (does the same trick as decode() method)
p2 = subprocess.run(["ls", "-la"], capture_output=True, text=True)

print(p2.stdout)
