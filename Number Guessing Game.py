import random
import math

lower = int(input("Enter the lower bound :- "))
upper = int(input("Enter the upper bound :- "))

computer_choise = random.randint(lower,upper)
print("You have only " , 
      round(math.log(upper - lower + 1,2)),
       "chances to guess the interger")

count = 0 

while count< math.log(upper - lower + 1,2):
    count +=1

    user_choise = int(input("Enter your choise:- "))

    if computer_choise == user_choise:
        print("Congratulation your guess the number in", count, " try")
        break
    elif computer_choise > user_choise:
        print("OOps !!! Your guessed number is too small!!")
    elif computer_choise < user_choise:
        print("OOps !!! Your guessed number is too high!!")

if count >= math.log(upper - lower + 1,2) :
    print("The number is : ", computer_choise)
    print("Better Luck Next Time!!!!!!") 