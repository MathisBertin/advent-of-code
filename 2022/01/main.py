# Part 1

def format_raw_calories(raw_calories):
    # remove the newline at the end and split for every new line
    string_calories = raw_calories.strip('\n').split('\n')
    # convert every item to int
    int_calories = map(int, string_calories)

    return int_calories


input = open('input.txt')
raw_calories_by_elfs = input.read().split('\n\n')
calories_by_elfs = map(format_raw_calories, raw_calories_by_elfs)
sum_calories_by_elfs = list(map(sum, calories_by_elfs))
total1 = max(sum_calories_by_elfs)
print(f'{total1=}')

# one liner
total1_bis = max(map(lambda e: sum(map(int, e.strip('\n').split('\n'))),
                 open('input.txt').read().split('\n\n')))
print(f'{total1_bis=}')


# Part 2
sum_calories_by_elfs.sort()
top_3_sum_calories = sum_calories_by_elfs[-3:]
total2 = sum(top_3_sum_calories)
print(f'{total2=}')
