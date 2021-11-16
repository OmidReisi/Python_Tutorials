courses = ["History", "Math", "Physics", "CompSci"]

print(courses)

print(len(courses))

print(courses[0])
print(courses[3])
print(courses[-1])

# error : index out of range
# print(courses[4])

print(courses[0:2])

courses.append("Art")
print(courses)

courses.insert(0, "Chemistery")
print(courses)

courses_2 = ["Bio", "Education"]

courses.extend(courses_2)
print(courses)

courses.remove("Math")
print(courses)


# removes and returns the value at index (default last)
courses.pop()
print(courses)


courses.pop(3)
print(courses)


courses.reverse()
print(courses)

courses.sort()
print(courses)

nums = [1, 5, 4, 3]
nums.sort()
print(nums)

nums.sort(reverse=True)
print(nums)

print(sorted(courses))

print(min(nums))
print(max(nums))
print(sum(nums))


print(courses.index("Art"))

print("Art" in courses)

for item in courses:
    print(item)

for index, course in enumerate(courses):
    print(index, course, sep=".")


course_str = ", ".join(courses)

print(course_str)

new_courses = course_str.split(", ")
print(new_courses)


list_1 = ["History", "Math", "Physics", "CompSci"]

# because list are mutable setting list_2 = list_1 means they are the same item with 2 different names
list_2 = list_1

print()
print()
print()

print(id(list_1))
print(id(list_2))


print(list_1)
print(list_2)

list_1.append("Art")

print(list_1)
print(list_2)

empty_list = []
empty_list =list()
