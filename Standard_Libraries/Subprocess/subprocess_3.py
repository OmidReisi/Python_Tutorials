import subprocess


# setting the capture_output = True is actually setting the stderr, stdout to subprocess.PIPE and we can do this manually ourself

p1 = subprocess.run(["ls", "-la"], stdout=subprocess.PIPE, text=True)


print(p1.stdout)


# we can redirect our stdout anywhere we want for example this is how we write our stdout to a file
with open(r"./stdout.log", "w") as f:
    p2 = subprocess.run(["ls", "-la"], stdout=f, text=True)

    # this returns None because we're not capturing our stdout in out subprocess.PIPE anymore
    print(p2.stdout)
