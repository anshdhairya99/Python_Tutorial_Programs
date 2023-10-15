
# Exercise -3 Number Guessing-----------------------------------------------------------------
# Question_-------------------------------------------------------
#n = 18
# no of guesses 9
# print no of guesses left
# No of guesses he took to finish
#game over-

# Solution:------------------------------------------------------------------------------------------------------
n= 18
number_of_guesses = 1
print("Number of guesses is limited to only 9 times:")
while(number_of_guesses<=9):
    guess_number = int(input("Guess the number😊:\n"))
    if guess_number<18:
        print("you enter less number please input greater number\n")
    elif guess_number>18:
        print("you enter greater number please input smaller number\n")
    else:
        print("You Won\n")
        print(number_of_guesses,"no. of Guesses he took to finish")
        break
    print(9-number_of_guesses,"no. of Guesses left" )
    number_of_guesses = number_of_guesses+1
    if(number_of_guesses>9):
        print("Game Over❌❌❌")





    



