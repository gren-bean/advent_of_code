"""
Advent of code
Day 2
"""

import utils as utils

def parse_data(data):
    parsed_data = {}
    cnt = 1

    # Parse data
    # Think of it like GAME => Matches => Points
    for line in data:
        # Everything after ':'
        game_data = line.strip().split(':')[1]

        # Split data by game
        # Example of match_data = [ "3 blue, 4 red", .... ]
        match_data = game_data.strip().split(';')

        match_data_parsed = []

        for m in match_data:
            # Example of color_info [ "3 blue", "4 red", .... ]
            points = m.strip().split(',')
            # Holds info match
            m_parsed = {}

            for p in points:
                info = p.strip().split(' ')
                m_parsed[info[1]] = int(info[0])

            match_data_parsed.append(m_parsed)

        parsed_data[cnt] = match_data_parsed
        cnt += 1

    # Example of parsed_data
    # 2: [{'blue': '12', 'red': '5'}, {'blue': '6', 'green': '5'}, ... {pull 3}, ... {pull 4}]
    return parsed_data


"""
Part1

"""
def p1():
    # data =  utils.read_input_strings('p1_test.txt')
    data = utils.read_input_strings('input.txt')
    parsed_data = parse_data(data)

    # Game constraints
    N = {'red': 12, 'green': 13, 'blue': 14}

    # Sum of game IDs that are possible
    game_id_sum = 0

    for game in parsed_data:
        possible_game = True
        for match in parsed_data[game]:
            for point_k in match.keys():
                if match[point_k] > N[point_k]:
                    possible_game = False

        if possible_game:
            game_id_sum += game

    print(game_id_sum)


"""
Part 2

The minimum number of cubes to play each game requires finding max points of each type
"""
def p2():
    # data = utils.read_input_strings('p2_test.txt')
    data = utils.read_input_strings('input.txt')
    parsed_data = parse_data(data)

    sum_of_powers = 0

    for game in parsed_data:
        # Reset maximums
        P = {'red': 0, 'green': 0, 'blue': 0}

        for match in parsed_data[game]:
            for point_k in match.keys():
                if match[point_k] > P[point_k]:
                    P[point_k] = match[point_k]

        power = P['red']*P['green']*P['blue']
        sum_of_powers += power

    print(sum_of_powers)

p1()
p2()