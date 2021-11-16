# Sets are unordered with no-duplicates

cs_courses = {"History", "Math", "Physics", "CompSci", "Math"}
print(cs_courses)

# sets are better optimized for membership tests than lists or tuples
print("Math" in cs_courses)

art_courses = {"History", "Math", "Art", "Design"}

print(cs_courses.intersection(art_courses))
print(cs_courses.difference(art_courses))
print(cs_courses.union(art_courses))


empty_set = set()
