# Day 2


def get_power(cubes_values: dict):
    colors = ["red", "green", "blue"]
    power = 1
    for color in colors:
        power *= max(cubes_values.get(color, [1]))

    return power


all_power_subsets = []

with open("input.txt", "r") as input:
    for line in input.readlines():
        line = line.split(":")
        subsets = line[1].split(";")

        print(subsets)

        all_cubes_total = {
            "red": [],
            "green": [],
            "blue": [],
        }

        for current_subset in subsets:
            for color in current_subset.split(","):
                color = color.split()
                color_count = int(color[0])
                color_name = color[1]

                for key, value in all_cubes_total.items():
                    if key == color_name:
                        all_cubes_total[key].append(color_count)

                print(color)
                print(color_count)
                print(color_name)
            print(all_cubes_total)
        all_power_subsets.append(get_power(cubes_values=all_cubes_total))

print(f"Sum of all powers: {sum(all_power_subsets)}")
