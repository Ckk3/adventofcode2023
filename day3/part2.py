numbers = []
all_valid_numbers_and_gear_ratios = {}


def check_if_number_is_a_valid_part_number(
    number: str, start_position: tuple, numbers_list: list
):
    # Check all positions if have some special char
    positions_to_test = [-1, 0, 1]
    all_gears = []
    for y in positions_to_test:
        for x_increment in range(len(number)):
            for x in positions_to_test:
                try:
                    current_char = str(
                        numbers_list[start_position[1] + y][
                            start_position[0] + x + x_increment
                        ]
                    )
                    if current_char.isnumeric() is False and current_char != ".":
                        return True, [
                            f"{start_position[1] + y}, {start_position[0] + x + x_increment}"
                        ]
                        # all_gears.append(
                        #     f"{start_position[1] + y}, {start_position[0] + x + x_increment}"
                        # )
                except IndexError:
                    continue
    # if len(all_gears) >= 1:
    #     return True, all_gears
    return False, None


with open("input.txt", "r") as input:
    for line in input.readlines():
        current_line = []
        for char in line:
            if char == "\n":
                char = "."
            current_line.append(str(char))
        numbers.append(current_line)


for y in range(0, len(numbers)):
    current_number = ""
    start_position = ()
    for x in range(len(numbers[0])):
        try:
            current_char = numbers[y][x]
            if str(current_char).isnumeric():
                if current_number == "":
                    start_position = (x, y)
                current_number += str(current_char)
                continue
            if current_number == "":
                continue

            result, all_gears = check_if_number_is_a_valid_part_number(
                number=current_number,
                start_position=start_position,
                numbers_list=numbers,
            )
            if result is True:
                for gear_position in all_gears:
                    try:
                        all_valid_numbers_and_gear_ratios[gear_position].append(
                            int(current_number)
                        )
                    except KeyError:
                        all_valid_numbers_and_gear_ratios[gear_position] = []
                        all_valid_numbers_and_gear_ratios[gear_position].append(
                            int(current_number)
                        )
            current_number = ""
            start_position = ()
        except IndexError:
            continue

valid_numbers = []
for gear, numbers in all_valid_numbers_and_gear_ratios.items():
    if len(numbers) >= 2:
        value = 1
        for num in numbers:
            value *= num
        valid_numbers.append(value)


print(f"The sum is {sum(valid_numbers)}")
