# when you import a file, you run everything in it
import my_module as mm


courses = ["History", "Math", "Physics", "CompSci"]

index = mm.find_index(courses, "Math")
print(index)
