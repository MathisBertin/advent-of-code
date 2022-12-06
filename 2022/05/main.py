import re

# Helpers
def parse_crates(crates):
    flipped_crates = list(reversed(list(crates)))
    number_of_columns = int(flipped_crates[0].split()[-1])
    parse_crates = [[] for _ in range(number_of_columns)]
    for height in range(1, len(flipped_crates)):
        for column in range(number_of_columns):
            letter = flipped_crates[height][column * 4 + 1]
            if letter != ' ':
                parse_crates[column].append(letter)
    return parse_crates

# Part 1
moves = open('moves.txt')
raw_crates = open('crates.txt')
crates = parse_crates(raw_crates)

for move in moves:
    number_of_moves, from_column, to_column = [int(n) for n in re.findall(r'-?\d+\.?\d*', move)]
    for i in range(number_of_moves):
        element = crates[from_column - 1].pop()
        crates[to_column - 1].append(element)
crates_on_top = ''.join([column[-1] for column in crates])
moves.close()
raw_crates.close()

print(f'{crates_on_top=}')

# Part 2
moves = open('moves.txt')
raw_crates = open('crates.txt')
crates = parse_crates(raw_crates)

for move in moves:
    number_of_moves, from_column, to_column = [int(n) for n in re.findall(r'-?\d+\.?\d*', move)]
    moved_item = crates[from_column - 1][-number_of_moves:]
    for i in range(number_of_moves):
        crates[from_column - 1].pop()
    crates[to_column - 1] += moved_item
crates_on_top2 = ''.join([column[-1] for column in crates])
print(f'{crates_on_top2=}')