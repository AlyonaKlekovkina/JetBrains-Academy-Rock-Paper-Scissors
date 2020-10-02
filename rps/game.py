import random


def update_name():
    file = open('rating.txt', 'r+')
    rating_dictionary = {}
    for line in file:
        the_line = line.split()
        n = the_line[0]
        r = the_line[1]
        rating_dictionary.update({n: int(r)})
    if name not in rating_dictionary:
        file.write(name + " " + '0' + '\n')
    file.close()
    return rating_dictionary


def current_rating():
    if name in name_and_rating:
        current_rating = name_and_rating[name]
        return current_rating
    else:
        return 0


def rock_paper_scissors(computer_option):
    win = {'rock': 'scissors', 'scissors': 'paper', 'paper': 'rock'}
    if users_option == computer_option:
        return 'draw'
    elif win[users_option] == computer_option:
        return 'win'
    else:
        return 'lose'


def more_options(computer_option):
    if users_option == computer_option:
        return 'draw'
    else:
        index = hand.index(users_option)
        the_list = hand[index+1:] + hand[:index]
        part = int(len(the_list) / 2)
        for i in range(len(the_list)):
            if (the_list[i] == computer_option) and (i >= part):
                return 'win'
            elif (the_list[i] == computer_option) and (i < part):
                return 'lose'


def get_game_result():
    if hand == ['']:
        computer_option = random.choice(['scissors', 'rock', 'paper'])
        the_result = rock_paper_scissors(computer_option)
        return computer_option, the_result
    else:
        computer_option = random.choice(hand)
        the_result = more_options(computer_option)
        return computer_option, the_result


name = input("Enter your name: ")
print("Hello, {}".format(name))
hand = input().split(',')
print("Okay, let's start")
name_and_rating = update_name()
the_rating = current_rating()

while True:
    users_option = input()
    list_of_options = hand + ['!rating'] + ['!exit'] + ['scissors'] + ['rock'] + ['paper']
    if users_option == '!exit':
        print("Bye!")
        break
    elif users_option not in list_of_options:
        print("Invalid input")
    elif users_option == '!rating':
        print("Your rating: ", the_rating)
    else:
        result = get_game_result()
        if result[1] == 'draw':
            the_rating += 50
            print("There is a draw ({})".format(users_option))
        elif result[1] == 'win':
            the_rating += 100
            print('Well done. The computer chose {} and failed'.format(result[0]))
        else:
            print('Sorry, but the computer chose {}'.format(result[0]))
