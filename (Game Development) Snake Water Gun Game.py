# (Game Development) Snake Water Gun Game :-----

import random
lst = ['s','w','g']

chance = 10
no_of_chance = 0
computer_point = 0
human_point = 0

print("\t \t \t \t Snake, Gun Game\n \n")
print("s for snake \nw for water \ng for gun \n")

# making the game in while:------ 
while no_of_chance < chance:
    _input = input('Snake Water,Gun:')
    _random = random.choice(lst)

    if _input == random:
        print("Tie Both 0 point to each \n")

    # if user enter s :------
    elif _input == "s" and _random =="g":
        computer_point = computer_point + 1
        print(f"your guess {_input} and computer guess is {_random} \n")
        print("Computer wins 1 point \n")
        print(f"computer_point is {computer_point} and your point is {human_point} \n")
    else:
        print("You have input wrong \n")
        no_of_chance = no_of_chance + 1
        print(f"{chance - no_of_chance} is left out of {chance} \n")

    print("GAME OVER!")

    if computer_point == human_point:
            print("Tie")

    elif computer_point > human_point:
            print("Computer Wins and You Loose")
    else:
            print("You Win and Computer Loose")
    print(f"your point is{human_point} and computer point is {computer_point}") 


