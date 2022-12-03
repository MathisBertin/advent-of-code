# Part 1
input = open('input.txt')

move_correspondances = {
    'X': 'A',
    'Y': 'B',
    'Z': 'C'
}
score1 = 0

for game in input:
    (opponent_move, my_move) = game.split()
    my_move = move_correspondances[my_move]
    score1 += 'ABC'.index(my_move) + 1
    if opponent_move == my_move:
        score1 += 3
    else:
        if 'ABC'.index(opponent_move) == 'BCA'.index(my_move):
            score1 += 6
input.close()
print(f'{score1=}')


# Part 2
input = open('input.txt')
score2 = 0

for game in input:
    (opponent_move, round_end) = game.split()
    if round_end == 'X':  # loose
        my_move = 'CAB'['ABC'.index(opponent_move)]
        score2 += 'ABC'.index(my_move) + 1
    elif round_end == 'Y':  # draw
        score2 += 'ABC'.index(opponent_move) + 1 + 3
    elif round_end == 'Z':  # win
        my_move = 'BCA'['ABC'.index(opponent_move)]
        score2 += 'ABC'.index(my_move) + 1 + 6


print(f'{score2=}')
