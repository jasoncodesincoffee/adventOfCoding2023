input = open('day1_input.txt', 'r')
lines = input.readlines()

def strToNum(string):
    match string:
        case 'one':
            return '1'
        case 'two':
            return '2'
        case 'three':
            return '3'
        case 'four':
            return '4'
        case 'five':
            return '5'
        case 'six':
            return '6'
        case 'seven':
            return '7'
        case 'eight':
            return '8'
        case 'nine':
            return '9'

num_list_original = []
num_list_final = []
is_num = True
#### THIS IS PART 1 ########
for line in lines:
    for letter in line:
        try:
            int(letter)
        except ValueError:
            is_num = False

        if is_num:
            num_list_original.append(letter)
        else:
            is_num = True
    combined_num = num_list_original[0] + num_list_original[-1]
    num_list_final.append(int(combined_num))
    num_list_original = []

answer1 = sum(num_list_final)
print(f'the answer for part 1 is: {answer1}')


### THIS IS PART 2 #####
validation = ['1','2','3','4','5','6','7','8','9','one','two','three',
              'four','five','six','seven','eight','nine']
num_list_final = []

for line in lines:
    h_position = -1
    l_position = 10000000000000

    for ele in validation:
        idx = line.find(ele)
        if idx != -1:
            if idx < l_position:
                first_number = ele
                l_position = idx
        idx = line.rfind(ele)
        if idx != -1:
            if idx > h_position:
                last_number = ele
                h_position = idx

    try:
        int(first_number)
    except ValueError:
        is_num = False

    if is_num:
        first_digit = first_number
    else:
        first_digit = strToNum(first_number)
        is_num = True

    try:
        int(last_number)
    except ValueError:
        is_num = False

    if is_num:
        second_digit = last_number
    else:
        second_digit = strToNum(last_number)
        is_num = True

    combined_num = first_digit + second_digit
    num_list_final.append(int(combined_num))

answer2 = sum(num_list_final)
print(f'the answer for part 2 is: {answer2}')