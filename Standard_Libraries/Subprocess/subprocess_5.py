import subprocess

p1 = subprocess.run(["cat", "./test.txt"], capture_output=True, text=True)

# print(p1.stdout)

# for commands like grep that search a file for the given content (here we're searching for "test" and -n represents the line number) you can pass a text instead of a file to search as the input argument
# here we're searching the output of our previous command for "test"
p2 = subprocess.run(
    ["grep", "-n", "test"], capture_output=True, text=True, input=p1.stdout
)

print(p2.stdout)

# this is the shortes version of above example
# now that you're using two command in a string you have to set the shell argument to True
p3 = subprocess.run(
    f"cat ./test.txt | grep -n test", capture_output=True, text=True, shell=True
)

print(p3.stdout)
