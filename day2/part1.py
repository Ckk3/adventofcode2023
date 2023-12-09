# Day 2

possible_games_ids = []

color_cubes_total = {
    "red": 12,
    "green": 13,
    "blue": 14,
}

with open("input.txt", "r") as input:
    for line in input.readlines():
        line = line.split(":")
        current_game_id = int(line[0].split()[1])
        subsets = line[1].split(";")

        print(current_game_id)
        print(subsets)

        try:
            for current_subset in subsets:
                for color in current_subset.split(","):
                    color = color.split()
                    color_count = int(color[0])
                    color_name = color[1]

                    for key, value in color_cubes_total.items():
                        if key == color_name:
                            if color_count > color_cubes_total[key]:
                                raise Exception("Not possible subset")

                    print(color)
                    print(color_count)
                    print(color_name)
            print("end possible game")
            possible_games_ids.append(current_game_id)
        except Exception as e:
            print(e)


print(f"Sum of possible games ids: {sum(possible_games_ids)}")
