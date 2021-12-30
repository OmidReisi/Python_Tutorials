# this module allows us to use external commands in python and see the results
import subprocess

# this run method runs the external command and puts the output in the terminal
# subprocess.run("ls")

# subprocess.run("dir", shell=True)

# shell is dangerous so use it if you're passing the command yourself and not reading from an input or someplace else
# subprocess.run("ls -la", shell=True)

# usually when we want to pass switches to our command we have to pass them as a list
p1 = subprocess.run(["ls", "-la"])

# returns the arguments passed to the run command (only arguments in the list or the single string input)
print(p1.args)

# returns the returncode of command and if there was any error (0 means no error)
print(p1.returncode)

# if the standard output is already sent to terminal (seeing the output of command in terminal) then this returns None
print(p1.stdout)
