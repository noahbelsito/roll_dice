from random import randint


def roll_dice():
    rolled = randint(1, 6)
    return rolled


print('Welcome to dice roll!')
print("Press 'r' to roll the dice or 'e' to exit")

user_input = input(': ').lower()
if user_input == 'e':
    print("You didn't even use the dice roller wtf?")
elif user_input == 'r':
    while True:
        print(roll_dice())
        user_input = input(': ').lower()
        if user_input == 'e':
            print('Goodbye!')
            break
else:
    print('Not an option idiot.')