'''AOC 2022 Day1'''
with open('Day1_input.txt') as f:
    lines = f.readlines()

list_of_calories_per_elf, total_list = [], []
for line in lines:
    if line != '\n':
        list_of_calories_per_elf.append(int(line))
    else:
        total = sum(list_of_calories_per_elf)
        total_list.append(total)
        list_of_calories_per_elf = []
print(max(total_list))

'''Part 2'''
sorted_list = sorted(total_list)
print(sorted_list[len(total_list) - 1] + sorted_list[len(total_list) - 2] + sorted_list[len(total_list) - 3])