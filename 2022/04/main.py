# Part 1
input = open('input.txt')


def is_included(section1, section2):
    start1, end1 = list(map(int, section1.split('-')))
    start2, end2 = list(map(int, section2.split('-')))
    first_in_second = start1 >= start2 and end1 <= end2
    second_in_first = start2 >= start1 and end2 <= end1
    return first_in_second or second_in_first


number_of_contained = 0

for pair in input:
    # Get the section of both pair
    section1, section2 = pair.split(',')
    section2 = section2.rstrip('\n')
    # Check if one section is included in the other
    if is_included(section1, section2) or is_included(section2, section1):
        number_of_contained += 1

print(f'{number_of_contained=}')

input.close()

# Part 2
input = open('input.txt')


def do_overlap(section1, section2):
    start1, end1 = list(map(int, section1.split('-')))
    start2, end2 = list(map(int, section2.split('-')))
    do_not_overlap = end1 < start2 or end2 < start1
    return not(do_not_overlap)


number_of_coverlap = 0

for pair in input:
    # Get the section of both pair
    section1, section2 = pair.split(',')
    section2 = section2.rstrip('\n')
    # Check if one section is included in the other
    if do_overlap(section1, section2) or do_overlap(section2, section1):
        number_of_coverlap += 1

print(f'{number_of_coverlap=}')

input.close()
