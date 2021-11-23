nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

my_list = []
for n in nums:
    my_list.append(n)

print(my_list)

# this does the same job as for loop above
my_list = [n for n in nums]
print(my_list)


my_list = []
for n in nums:
    my_list.append(n * n)

print(my_list)

my_list = [n * n for n in nums]
print(my_list)

my_list = map(lambda n: n * n, nums)
# this is no longer a list but an iterator and should be used with for loop
print(my_list)

# for n in my_list:
#     print(n)


# my_list = ["hello" for n in range(10)]
# print(my_list)


my_list = [n for n in nums if n % 2 == 0]
print(my_list)

my_list = filter(lambda n: n % 2 == 0, nums)

# for n in my_list:
#     print(n)

my_list = [(letter, number) for letter in "abcd" for number in range(4)]
print(my_list)


names = ["Bruce", "Clark", "Peter", "Logan", "Wade"]
heros = ["Batman", "Superman", "Spiderman", "Wolverine", "Deadpool"]

print(list(zip(names, heros)))
print()

my_dict = {name: hero for name, hero in zip(names, heros)}
print(my_dict)


my_dict = {
    name: hero
    for (name, hero) in zip(names, heros)
    if name != "Peter" and hero != "Superman"
}
print(my_dict)


nums = [1, 1, 2, 1, 3, 4, 3, 5, 5, 6, 7, 8, 7, 9, 9]

my_set = {n for n in nums}
print(my_set)

new_nums = [n for n in set(nums)]
print(new_nums)

# we don't have tuple comprehensions instead we can create generators by using ()
my_gen = (n * n for n in new_nums)
print(my_gen)

for i in my_gen:
    print(i)
