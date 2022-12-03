# Helper
def get_priority(char):
    if char.islower():
        return ord(char) - 96
    else:
        return ord(char) - 64 + 26


# Part 1
input = open('input.txt')

priorities_sum1 = 0

for rucksack in input:
    # Get the duplicate item
    rucksack = rucksack.strip('\n')
    first_compartment = set(rucksack[0:len(rucksack)//2])
    second_compartment = set(rucksack[len(rucksack)//2:])
    duplicate_item = first_compartment.intersection(second_compartment).pop()

    # Get its priority value
    priorities_sum1 += get_priority(duplicate_item)

input.close()

print(f'{priorities_sum1=}')


# Part 2
input = open('input.txt')
priorities_sum2 = 0

for rucksack1 in input:
    rucksack1 = set(rucksack1.strip('\n'))
    rucksack2 = set(input.readline().strip('\n'))
    rucksack3 = set(input.readline().strip('\n'))
    badge = rucksack1.intersection(rucksack2, rucksack3).pop()
    priorities_sum2 += get_priority(badge)

print(f'{priorities_sum2=}')
