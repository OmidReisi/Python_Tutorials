employees = ["Corey", "Jim", "Steven", "April", "Judy", "Jenn", "John", "Jane"]

gym_members = ["April", "John", "Corey"]

developers = ["Judy", "Corey", "Steven", "Jane", "April"]

result = set(gym_members).intersection(developers)
print(result)

result = set(employees).difference(gym_members, developers)
print(result)
