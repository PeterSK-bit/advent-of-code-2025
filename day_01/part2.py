with open("day_01/input.txt", "r") as f:
    instructions = [(line[0], int(line[1:])) for line in f]

dial = 50
counter = 0

for direction, number in instructions:
    if direction == "R":
        first = (100 - dial) or 100 

        if first <= number:
            counter += 1 + (number - first) // 100

        dial = (dial + number) % 100

    elif direction == "L":
        first = dial or 100 

        if first <= number:
            counter += 1 + (number - first) // 100

        dial = (dial - number) % 100

print(counter)

# 6738