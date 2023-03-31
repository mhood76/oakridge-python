from random import randrange

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
print(secret_number)
