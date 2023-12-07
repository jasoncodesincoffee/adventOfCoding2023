input = open('day3_input.txt', 'r')
lines = input.readlines()

rows = []
search_window = (-1,0,1)
number_map = []
accumulator = []
is_num = True

for line in lines:
    line = line.rstrip('\n')
    rows.append(line)

### THIS IS PART 1 #################
for count_row, row in enumerate(rows):
    for idx, column in enumerate(row):
        if not column.isalnum() and column != '.':
            for y in search_window:
                for x in search_window:
                    try:
                        int(rows[count_row+y][idx+x])
                        is_num = True
                    except ValueError:
                        is_num = False

                    if is_num:
                        string_num_list = []
                        string_num_list.append(rows[count_row+y][idx+x])
                        current_position = idx+x-1
                        next_column = rows[count_row+y][current_position]
                        while next_column.isnumeric() and current_position >= 0:
                            string_num_list.insert(0,rows[count_row+y][current_position])
                            current_position -= 1
                            next_column = rows[count_row+y][current_position]
                        current_position = idx+x+1
                        next_column = rows[count_row + y][current_position]
                        while next_column.isnumeric() and current_position < len(row):
                            string_num_list.append(rows[count_row+y][current_position])
                            current_position += 1
                            if current_position < len(row):
                                next_column = rows[count_row+y][current_position]
                        string_num = map(str, string_num_list)
                        string_num = ''.join(string_num)
                        if len(accumulator) > 0 and int(string_num) != accumulator[-1]:
                            accumulator.append(int(string_num))
                        elif len(accumulator) == 0:
                            accumulator.append(int(string_num))

print(f'the accumulated value is {sum(accumulator)}')

### THIS IS PART 2 ###############
