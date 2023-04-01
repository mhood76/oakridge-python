from random import randrange
import time

def quit_game():
    print("Good Bye!")
    quit()

'''
Added a `While` Loop and `If` statement to make sure
We only accept Y or N as answers.
'''
while True:
    answer = input("Do you want to play? (Y/N) ")
    if answer in ['Y', 'N']: 
        break
    print("I did not understand, Enter Y for Yes or N for No!")
    
if answer == 'N':
    quit_game()
    
print("You get 3 tries to guess the random number between 0 and 10")

secret_number = randrange(0, 10, 1)

trys = 3

for t in range(0, trys):
    guess = int(input(f"Attempt #{t+1}, What is your choice? "))
    time.sleep(1)
    print("hmmm... let me check if you are correct")
    time.sleep(1)

    if guess == secret_number:
        print("Wow!!! You got it right! Congrats!")
        quit_game()

    print("Nope, that was not the correct number")

print("Sorry you did not guess the correct number... :(")
print(f"The correct answer was {secret_number}.")
quit_game()
