input = open('day5_input.txt', 'r')
lines = input.readlines()

def follow_map(map_dict, map_idx, stages, current_val):
    map_idx += 1
    if map_idx == len(stages):
        return current_val
    else:
        for row in map_dict[stages[map_idx]]:
            if current_val >= row[1] and current_val <= row[1] + row[2]-1:
                diff = current_val - row[1]
                current_val = row[0] + diff
                # print(f'the current stage is {stages[map_idx]} with a value of {current_val}')
                current_val = follow_map(map_dict, map_idx, stages, current_val)
                return current_val
        if map_idx != len(stages):
            # print(f'the current stage is {stages[map_idx]} with a value of {current_val}')
            current_val = follow_map(map_dict, map_idx, stages, current_val)
            return current_val


def create_new_seed_list(old_seed_list):
    new_seed_list = []
    for i, seed in enumerate(old_seed_list):
        if i % 2:
            temp_seed_val = old_seed_list[i-1]
            for x in range(old_seed_list[i]):
                new_seed_list.append(temp_seed_val)
                temp_seed_val += 1
    return new_seed_list

### THIS IS PART 1 #########
has_mapping = False
almanac = {}
map_order = ['seeds', 'soil', 'fertilizer', 'water', 'light', 'temperature', 'humidity', 'location']
map_index = 0
location_found = False

# SETTING UP MAPPINGS IN LISTS
for line in lines:
    line = line.strip()
    if line != '' and line[-1] != ':' and line[0].isalpha():
        temp_seeds_label = line.split(': ')
        temp_seeds = temp_seeds_label[1].split(' ')
        numbers = [int(x) for x in temp_seeds]
        almanac['seeds'] = []
        for x in numbers: almanac['seeds'].append(x)
    elif line != '' and line[0].isnumeric():
        temp_arry = line.split(' ')
        numbers = [int(x) for x in temp_arry]
        if not map_order[map_index] in almanac:
            almanac[map_order[map_index]] = []
        almanac[map_order[map_index]].append(numbers)
    elif line != '' and line[0].isalpha():
        map_index += 1

# NOW TO USE MAPS TO TRACK SEED TO LOCATION
best_location_list = []
map_index = 0
for seed in almanac['seeds']:
    best_location = follow_map(almanac, map_index, map_order, seed)
    best_location_list.append(best_location)
best_location_list.sort()
print(f'The answer to part 1 is {best_location_list[0]}')

### THIS IS PART 2 ##############
# new_seeds = create_new_seed_list(almanac['seeds'])
# almanac['seeds'] = new_seeds
# best_location_list = []
# map_index = 0
# for seed in almanac['seeds']:
#     best_location = follow_map(almanac, map_index, map_order, seed)
#     best_location_list.append(best_location)
# best_location_list.sort()
# print(f'The answer to part 2 is {best_location_list[0]}')


best_location_list = []
map_index = 0
for i, seed in enumerate(almanac['seeds']):
    if i % 2 and i > 0:
        seed = almanac['seeds'][i-1]
        for x in range(almanac['seeds'][i]):
            best_location = follow_map(almanac, map_index, map_order, seed)
            best_location_list.append(best_location)
            seed += 1
best_location_list.sort()
print(f'The answer to part 1 is {best_location_list[0]}')