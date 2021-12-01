# the else caluse on loops runs if no break is hit in the loop
# even if a break statement exists in the loop but we don't hit it the else caluse runs


my_list = [1, 2, 3, 4, 5]

for i in my_list:
    print(i)

    # this break doesn't hit so else caluse runs
    if i == 7:
        break

else:
    print("Hit the For/Else Statement")

print()
print()
length = 0

while length < len(my_list):

    if length == 3:
        break
    print(my_list[length])

    length += 1
else:
    print("while loop else caluse")
