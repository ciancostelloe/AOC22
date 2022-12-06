'''AOC 2022'''
'''Day 1.1'''
with open('Day1_input.txt') as f:
    lines = f.readlines()

list_of_calories_per_elf, total_list = [], []
for line in lines:
    if line != '\n':
        list_of_calories_per_elf.append(int(line))
    else:
        list_of_calories_per_elf = []
    if list_of_calories_per_elf:
        total = sum(list_of_calories_per_elf)
        total_list.append(total)
answer = max(total_list)
print(answer)
    
    