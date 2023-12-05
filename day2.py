input = open('day2_input.txt', 'r')
lines = input.readlines()
game_list = []
cube_game_set = {
    "red": 12,
    "green": 13,
    "blue": 14
}
the_impossible_list = []
current_set = {}

def cubes(set_list):
    for set in set_list:
        cubes = set.split(",")
        for cube in cubes:
            color = cube.split(" ")
            color.remove("")
            match color[1]:
                case 'blue':
                    current_set["blue"] = int(color[0])
                case 'green':
                    current_set["green"] = int(color[0])
                case 'red':
                    current_set["red"] = int(color[0])

def sum_of_games(lines):
    game_info = lines[0].split(":")
    game_num = game_info[0].split(" ")[1]
    first_num = int(game_num)

    game_info = lines[-1].split(":")
    game_num = game_info[0].split(" ")[1]
    last_num = int(game_num)
    return first_num, last_num

for line in lines:
    current_set.clear()
    line = line.rstrip("\n")
    game_info = line.split(":")
    game_num = game_info[0].split(" ")[1]
    game_set = game_info[1].split(";")
    for set in game_set:
        each_cube_set = set.split(",")
        cubes(each_cube_set)
        if "blue" in current_set and current_set['blue'] > cube_game_set['blue']:
            the_impossible_list.append(int(game_num))
            break
        if "green" in current_set and current_set['green'] > cube_game_set['green']:
            the_impossible_list.append(int(game_num))
            break
        if "red" in current_set and current_set['red'] > cube_game_set['red']:
            the_impossible_list.append(int(game_num))
            break

print(sum(the_impossible_list))

first_num, last_num = sum_of_games(lines)
total_game_sum = len(lines)*(first_num + last_num)/2
possible_list_total = total_game_sum - sum(the_impossible_list)
print(int(possible_list_total))