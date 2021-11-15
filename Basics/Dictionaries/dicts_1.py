# keys can be strings or integers or some other data types
student = {"name": "John", "age": 25, "courses": ["Math", "CompSci"]}
print(student)
print(student["courses"])

# get method returns the value of the key or the specified value (default : None)
print(student.get("Phone", "Not Found"))

# creates or updates the key and value
student["Phone"] = "555-555"
print(student)

student.update({"name": "Jane", "age": 26})
print(student)


del student["age"]
print(student)

name = student.pop("name")
print(student, name, sep="\n")

# number of keys
print(len(student))

print(student.keys())
print(student.values())
print(student.items())


for key, value in student.items():
    print(key, value, sep=" : ")
