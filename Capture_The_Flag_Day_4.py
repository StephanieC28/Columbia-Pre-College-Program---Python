# flag1: Create a list of 5 different fruits
fruits = ["apple", "banana", "cherry", "date", "elderberry"]

# flag2: Print the 3rd fruit in the list
print(fruits[2])

# flag3: Add "fig" to the list and print the updated list
fruits.append("fig")
print(fruits)

# flag4: Remove the first fruit from the list and print
del fruits[0]
print(fruits)

# flag5: Use a loop to print only fruits that contain the letter "a"
for item in fruits:
    if "a" in item:
        print(item)

# flag 6: Create a new list containing the length of eac fruit name
lengths = []
for fruit in fruits:
    count = 0
    for char in fruit:
        count += 1

    new_lengths = [0] * (len(lengths) + 1)
    for i in range(len(lengths)):
        new_lengths[i] = lengths[i]
    new_lengths[len(lengths)] = count
    lengths = new_lengths

for n in lengths:
    print(n, end=" ")
print()

# flag 7: Find the longest fruit name and print it
longest = fruits[0]
max_length = 0
for c in longest:
    max_length += 1

for i in range(1, len(fruits)):
    count = 0
    for char in fruits[i]:
        count += 1
    if count > max_length:
        longest = fruits[i]
        max_length = count

print("Longest fruit:", longest)
