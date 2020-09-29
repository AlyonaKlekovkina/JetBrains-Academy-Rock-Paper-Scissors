import random

# Write your code here
users_option = input()
options = ['scissors', 'rock', 'paper']
computer_option = random.choice(options)

if users_option == computer_option:
    print("There is a draw ({})".format(users_option))
elif (users_option == 'rock' and computer_option == 'scissors') or (users_option == 'paper' and computer_option == 'rock') or (users_option == 'scissors' and computer_option == 'paper'):
    print("Well done. The computer chose {} and failed".format(computer_option))
else:
    print("Sorry, but the computer chose {}".format(computer_option))
