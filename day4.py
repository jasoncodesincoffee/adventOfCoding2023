input = open('day4_input.txt', 'r')
lines = input.readlines()

def card_copies(pile, num_matches, idx):
    for match in range(num_matches):
        next_index = match+1+int(idx)
        if not str(next_index) in pile:
            card_pile[str(next_index)] = 1
        else:
            card_pile[str(next_index)] += 1
    return card_pile

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
card_pile = {}
for idx, line in enumerate(lines):
    cards = line.split(':')
    card_num = cards[0].split(' ')
    card_num = card_num[-1]
    if not card_num in card_pile:
        card_pile[card_num] = 1
    else:
        card_pile[card_num] += 1
    games = cards[1].split('|')
    winning_cards = games[0].strip()
    winning_cards_list = winning_cards.split(' ')
    my_cards = games[1].strip()
    my_cards_list = my_cards.split(' ')

    matches = set(winning_cards_list).intersection(my_cards_list)
    if '' in matches:
        matches.remove('')
    if matches:
        card_pile = card_copies(card_pile, len(matches), card_num)
        for card in range(int(card_pile[card_num])-1):
            card_pile = card_copies(card_pile, len(matches), card_num)

total = sum(card_pile.values())
print(f'The answer to part 2 is {total}')