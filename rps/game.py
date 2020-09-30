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
        file.write('\n' + name + " " + '0' + '\n')
    file.close()
    return rating_dictionary


def update_rating(score):
    rating_dictionary = update_name()
    file = open('rating.txt', 'r+')
    file.write(name + ' ' + str(rating_dictionary[name] + int(score)) + '\n')
    file.close()


# Write your code here
name = input("Enter your name: ")
print("Hello, {}".format(name))
while True:
    name_and_rating = update_name()
    users_option = input()
    computer_option = random.choice(['scissors', 'rock', 'paper'])
    win = {'rock': 'scissors', 'scissors': 'paper', 'paper': 'rock'}
    list_of_options = ['!rating', '!exit', 'scissors', 'rock', 'paper']

    if users_option == '!exit':
        print("Bye!")
        break
    elif users_option not in list_of_options:
        print("Invalid input")
    elif users_option == '!rating':
        name_and_rating = update_name()
        print("Your rating: ", name_and_rating[name])
    elif users_option == computer_option:
        update_rating(50)
        print("There is a draw ({})".format(users_option))
    elif win[users_option] == computer_option:
        update_rating(100)
        print("Well done. The computer chose {} and failed".format(computer_option))
    elif win[users_option] != computer_option:
        print("Sorry, but the computer chose {}".format(computer_option))
