def pt1():
    f = open("day4.txt", "r") 
    whole_input = f.readlines() 

    all_points = []

    for line in whole_input: 
        card_points = 0

        winning_numbers = ((line.split(": ")[1]).split(" | ")[0]).split()
        owned_numbers = ((line.split(": ")[1]).split(" | ")[1]).split()

        for number in owned_numbers:
            if number in winning_numbers and card_points == 0:
                card_points = 1
            elif number in winning_numbers:
                card_points *= 2

        if card_points != 0:
            all_points.append(card_points)

    print(sum(int(i) for i in all_points))

def pt2():
    f = open("day4.txt", "r") 
    whole_input = f.readlines()

    all_cards = [1 for i in range(len(whole_input))]

    for line in whole_input: 
        card_matches = 0

        winning_numbers = ((line.split(": ")[1]).split(" | ")[0]).split()
        owned_numbers = ((line.split(": ")[1]).split(" | ")[1]).split()

        for number in owned_numbers:
            if number in winning_numbers:
                card_matches += 1

        for copy in range(all_cards[whole_input.index(line)]):
            a = 1  # a helping valuable for calculating the indexes of the cards that should have a new copy
            for i in range(card_matches):
                all_cards[whole_input.index(line) + a] += 1
                a += 1

    print(sum(all_cards))
pt1()
pt2()