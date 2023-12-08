input = open('day4_input.txt', 'r')
lines = input.readlines()

### THIS IS PART 1 #################
score = 0
for line in lines:
    remove_titles = line.split(':')
    games = remove_titles[1].split('|')
    winning_cards = games[0].strip()
    winning_cards_list = winning_cards.split(' ')
    my_cards = games[1].strip()
    my_cards_list = my_cards.split(' ')

    matches = set(winning_cards_list).intersection(my_cards_list)
    if '' in matches:
        matches.remove('')
    if matches:
        bit_counter = [0 for match in matches]
        bit_counter[0] = 1
        binary = ''.join(str(bits) for bits in bit_counter)
        score += int(binary,2)

print(f'The answer for part 1 is {score}')

### THIS IS PART TWO ##############