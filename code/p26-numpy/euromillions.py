import random

my_numbers = [3, 4, 12, 34, 40]
my_stars = [3, 7]

my_combination = f"{my_numbers} : {my_stars}"
print(my_combination)





counter = 0
while True:
    counter += 1
    if counter % 100000 == 0:
        print(counter)
    game_numbers = sorted(random.sample(range(1, 51), 5))
    game_stars = sorted(random.sample(range(1, 13), 2))
    game_combination = f"{game_numbers} : {game_stars}"

    if my_combination == game_combination:
        break

print("You won")
print(f"it took {counter} tries")



