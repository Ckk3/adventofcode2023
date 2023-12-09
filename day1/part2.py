# Day 2

numbers_names = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}
numbers = []

with open("input.txt") as text:
    for line in text.readlines():
        current_line = []
        pos = 0
        last_number_pos = 0
        for char in line:
            try:
                current_line.append(int(char))
                last_number_pos = pos + 1
            except ValueError:
                current_text_without_numbers = line[last_number_pos : pos + 1]
                for key, value in numbers_names.items():
                    if key in current_text_without_numbers:
                        current_line.append(value)
                        last_number_pos = pos
                        break
            pos += 1
        numbers.append(int(f"{current_line[0]}{current_line[-1]}"))


print(f"the sum of all of the calibration values is: {sum(numbers)}")
