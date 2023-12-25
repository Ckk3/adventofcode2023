all_cards_points = []


def calculate_card_points(winning_numbers, numbers_i_have):
    total_numbers_quant = 0
    for number in numbers_i_have:
        if number in winning_numbers:
            if total_numbers_quant == 0:
                total_numbers_quant = 1
                continue
            total_numbers_quant *= 2

    return total_numbers_quant


with open("input.txt", "r") as input:
    for line in input.readlines():
        card = line.split(":")[1]
        winning_numbers = card.split("|")[0].strip().split(" ")
        numbers_i_have = card.split("|")[1].strip().replace("\n", "").split(" ")

        winning_numbers = [int(num.strip()) for num in winning_numbers if num != ""]
        numbers_i_have = [int(num.strip()) for num in numbers_i_have if num != ""]
        all_cards_points.append(calculate_card_points(winning_numbers, numbers_i_have))


print(f"Sum of all points: {sum(all_cards_points)}")
