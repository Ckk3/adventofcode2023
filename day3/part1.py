numbers = []
all_valid_numbers = []


def check_if_number_is_a_valid_part_number(
    number: str, start_position: tuple, numbers_list: list
):
    # Check all positions if have some special char
    positions_to_test = [-1, 0, 1]
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
                        return True
                except IndexError:
                    continue


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
            if (
                check_if_number_is_a_valid_part_number(
                    number=current_number,
                    start_position=start_position,
                    numbers_list=numbers,
                )
                is True
            ):
                all_valid_numbers.append(int(current_number))
            current_number = ""
            start_position = ()
        except IndexError:
            continue

print(f"The sum is {sum(all_valid_numbers)}")
