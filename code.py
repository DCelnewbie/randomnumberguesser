import random

def getNumber():
    return random.randint(1,1001)

def getGuess():
    return int(input(""))

def game(pcNumber):
    guess = getGuess()
    if pcNumber < guess:
        print(f"The number {guess} is bigger than the number.")
        game(pcNumber)
    elif pcNumber > guess:
        print(f"The number {guess} is lower than the number.")
        game(pcNumber)
    else:
        print(f"You got it right! The number was {guess}")

def getRestart():
    restart = input("Wanna play again? ")
    if restart not in ["yes","no"]:
        print("Huh?")
        getRestart()
    elif restart == "yes":
        main()
    else:
        return
    
def  main():
    pcNumber= getNumber()
    game(pcNumber)
    getRestart()
    
main()
