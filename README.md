# Random Number Guesser









import random 
pcNumber = random.randint(0,101)
while True:
    personNumber = int(input("chose a number: "))
    if personNumber < pcNumber:
        print("the number is greater than", personNumber)
    elif  personNumber > pcNumber:
        print("the number is lower than", personNumber)
    else:
        print("congrats, you got it right.")
        playAgain = input("wanna play again? ")
        if playAgain == "no":
            print("okay, thanks for playing.")
            break
        else:
            pcNumber = random.randint(0,101)
