from random import randrange
import time

def quit_game():
    print("Good Bye!")
    exit()


secret = randrange(0, 10, 1)
trys = 3
rules = '''
#########################################################
# You get 3 tries to guess the random number between    #
# 0 and 10.                                             #  
#########################################################

'''



while True:
    play = input('This game is called "Guess the Random Number." Do you want to play (Yes/No)? ' )
    if play.lower() == "yes" or play.lower() == "no":
        print(rules)
        break
    else:
        print("You did not enter 'Yes' or 'No'! Try again!!!")

if play.lower() == "no":
    quit_game()

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
quit_game()
