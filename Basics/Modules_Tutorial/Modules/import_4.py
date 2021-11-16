# when you import a file, you run everything in it
from my_module import find_index as fi, test


courses = ["History", "Math", "Physics", "CompSci"]

index = fi(courses, "Math")
print(index)

print(test)
