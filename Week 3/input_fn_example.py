x = int(input("Please input a number: "))
b = int(input("Please input a second number: "))

a = input("Do you want to add or subtract? (add/subtract): ")

if a == 'add':
    answer = x+b
    
elif a == 'subtract':
    answer = x-b

else:
    answer = "You did not type in the correct response."
    
print(answer)