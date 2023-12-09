# Day 1

numbers = []

with open("input.txt") as text:
    for line in text.readlines():
        current_line = []
        pos = 0
        last_number_pos = 0
        for char in line:
            try:
                current_line.append(int(char))
                last_number_pos = pos
            except ValueError:
                pass

            pos += 1
        numbers.append(int(f"{current_line[0]}{current_line[-1]}"))


print(f"the sum of all of the calibration values is: {sum(numbers)}")
