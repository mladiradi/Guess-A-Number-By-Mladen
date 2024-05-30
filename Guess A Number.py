
import  random

computer_number = random.randint(1, 100)

while True:
    print()
    player_input = input("Guess the number between 1 and 100: ")
    print()

    if not player_input.isdigit():
        print("Your input is not valid !")
        print()
        print("Please try again !")
        print()
        continue

    player_number = int(player_input)

    if player_number == computer_number:
        print("Congratulations ! You guess the number !")
        break
    elif player_number > computer_number:
        print("The number you choose is too high !")
    else:
        print("The number you choose is too low !")
