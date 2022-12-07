# Helpers

def get_index_first_n_distinct_char(message: str, n: int):
    for i in range(n, len(message) + 1):
        sequence =set(message[i-n:i])
        if len(sequence) == n:
            return i
    return -1

# Part 1
datastream = open('input.txt').read()
index = get_index_first_n_distinct_char(datastream, 4)
print(f'First start-of-packet marker: {index}')

# Part 2
index = get_index_first_n_distinct_char(datastream, 14)
print(f'First start-of-message marker: {index}')