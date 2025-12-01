with open("day_01/input.txt", "r") as f:
    instructions = [(line[0], int(line[1:])) for line in f.readlines()]

dial = 50 # 0-99
counter = 0

for direction, number in instructions:
    if direction == "L":
        number = -number
    
    dial += number

    if dial % 100 == 0:
        counter += 1

print(counter)