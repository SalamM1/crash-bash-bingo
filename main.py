import csv
import random
import json


def get_data_file():
    filename = 'data/cbash-bingo-data.csv'

    with open(filename, newline='') as f:
        csv_reader = csv.reader(f)
        fileData = next(csv_reader)

    return fileData[1:]


def get_config_file():
    filename = 'data/cbash-bingo-config.json'
    with open(filename) as f:
        config_data = json.load(f)

    return config_data


def handle_exclusions(warpRooms, bosses, levelTypes, collectibles, excluded_levels, included_levels, fileData):
    if not warpRooms[0]:
        excluded_levels = excluded_levels.union(
            {fileData[0], fileData[4], fileData[8], fileData[12], fileData[28]}
        )
    if not warpRooms[1]:
        excluded_levels = excluded_levels.union(
            {fileData[1], fileData[5], fileData[9], fileData[13], fileData[16], fileData[29]}
        )
    if not warpRooms[2]:
        excluded_levels = excluded_levels.union(
            {fileData[2], fileData[6], fileData[10], fileData[14], fileData[17], fileData[20], fileData[30]}
        )
    if not warpRooms[3]:
        excluded_levels = excluded_levels.union(
            {fileData[3], fileData[7], fileData[11], fileData[15], fileData[18], fileData[21], fileData[24], fileData[31]}
        )
    if not warpRooms[4]:
        excluded_levels = excluded_levels.union(
            {fileData[22], fileData[25], fileData[26], fileData[19], fileData[27], fileData[23]}
        )

    if not bosses:
        excluded_levels = excluded_levels.union(
            set(fileData[28:32])
        )

    if not levelTypes[0]:
        excluded_levels = excluded_levels.union(set(fileData[0:4]))
    if not levelTypes[1]:
        excluded_levels = excluded_levels.union(set(fileData[4:8]))
    if not levelTypes[2]:
        excluded_levels = excluded_levels.union(set(fileData[8:12]))
    if not levelTypes[3]:
        excluded_levels = excluded_levels.union(set(fileData[12:16]))
    if not levelTypes[4]:
        excluded_levels = excluded_levels.union(set(fileData[16:20]))
    if not levelTypes[5]:
        excluded_levels = excluded_levels.union(set(fileData[20:24]))
    if not levelTypes[6]:
        excluded_levels = excluded_levels.union(set(fileData[24:28]))

    if not collectibles[0]:
        excluded_levels = excluded_levels.union([fileData[32]])
    if not collectibles[1]:
        excluded_levels = excluded_levels.union([fileData[33]])
    if not collectibles[2]:
        excluded_levels = excluded_levels.union([fileData[34]])
    if not collectibles[3]:
        excluded_levels = excluded_levels.union([fileData[35]])
    if not collectibles[4]:
        excluded_levels = excluded_levels.union([fileData[36]])

    return set(excluded_levels) - set(included_levels)


def get_crashbash_bingo(exclusions, bingo_quant, fileData):
    levelNames = frozenset(set(fileData[0:28]) - exclusions)
    bosses = frozenset(set(fileData[28:32]) - exclusions)
    objectives = frozenset(set(fileData[32:]) - exclusions)

    bingoSlots = []

    for level in levelNames:
        for objective in objectives:
            bingoSlots.append(level + ' ' + objective)

    if 'bosses' not in exclusions:
        bingoSlots += bosses
    random.shuffle(bingoSlots)

    return list(set(bingoSlots) - exclusions)[:bingo_quant]

# PROCESSING
file_data = get_data_file()
config_data = get_config_file()
exclusions = handle_exclusions(
    config_data.get('warp_rooms'), config_data.get('bosses'), config_data.get('game_types'),
    config_data.get('collectibles'), set(config_data.get('excluded_levels')), set(config_data.get('included_levels')), file_data
)
bingoSlots = get_crashbash_bingo(exclusions, 25, file_data)

# WRITING TO FILE
x = []
for bingo in bingoSlots:
    x.append({"name": bingo})

x = json.dumps(x)
with open("crashbash-bingo.json", "w+") as f:
    f.write(x)
print(x)