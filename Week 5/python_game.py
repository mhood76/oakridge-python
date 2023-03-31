from random import randrange

def quit_game():
    print("Good Bye!")
    quit()

answer = input("Do you want to play? (Y/N) ")

if answer == "N":
    quit_game()
    
print("You get 3 tries to guess the random number between 0 and 10")

secret_number = randrange(0, 10, 1)
print(secret_number)
