import random
 
num = random.randint(1, 3)
guess = int(input("guess a number between 1 to 3: "))
print("your number is: ",guess)
print("the number is: ", num)        

if(num == guess):
    print("you won!")
else:
    print("you loose")
