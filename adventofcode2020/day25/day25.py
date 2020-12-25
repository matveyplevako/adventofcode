with open('input.txt') as inp:
    card, door = map(int, inp.readlines())

value = 1

card_loop_number = 0
door_loop_number = 0

while value != card:
    value = (7 * value) % 20201227
    card_loop_number += 1

value = 1
while value != door:
    value = (7 * value) % 20201227
    door_loop_number += 1

print(card_loop_number)
print(door_loop_number)

value = 1
for i in range(card_loop_number):
    value = (door * value) % 20201227

print(value)

value = 1
for i in range(door_loop_number):
    value = (card * value) % 20201227

print(value)

