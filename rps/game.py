import random

# Write your code here
while True:
    users_option = input()
    computer_option = random.choice(['scissors', 'rock', 'paper'])
    win = {'rock': 'scissors', 'scissors': 'paper', 'paper': 'rock'}

    if users_option == '!exit':
        print("Bye!")
        break
    elif users_option not in win:
        print("Invalid input")
    elif users_option == computer_option:
        print("There is a draw ({})".format(users_option))
    elif win[users_option] == computer_option:
        print("Well done. The computer chose {} and failed".format(computer_option))
    elif win[users_option] != computer_option:
        print("Sorry, but the computer chose {}".format(computer_option))


