from random import randrange
import time


secret = randrange(0, 10, 1)
trys = 3
rules = '''
#########################################################
# This game is called "Guess the Random Number"         #
# You get 3 tries to guess the random number between    #
# 0 and 10.                                            #  
#########################################################
'''

print(rules)

while True:
    play = input("Do you want to play (Yes/No)? " )
    if play.lower() == "yes" or play.lower() == "no":
        break
    else:
        print("Did not enter 'Yes' or 'No'! Try again!!!")

if play.lower() == "no":
    print("Good Bye!")
    exit()

print("A random number has been generated")
print("Can you guess it in 3 tries? \n")

for t in range(0, trys):
    guess = int(input(f"Attempt #{t+1}, What is your choice? "))
    time.sleep(1)
    print("hmmm... let me see")
    time.sleep(2)

    if guess == secret:
        print("Wow!!! You got it right! Congrats!")
        quit()
    print("Nope that was not the number")

print("Sorry you did not guess the correct number... :(")
print(f"The correct answer was {secret}. Better luck next time.")
