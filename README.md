# Random Number Guesser
Random generator number python game, which the user needs to guess the random number.
This is one of the simple python projects yet an exciting one. You can even call it a mini-game. It is a program in which the computer randomly chooses a number between 1 to 100, or any range that you would like to. Then give users a hint to guess the number. Every time the user guesses wrong, he gets another clue. The clue is if the computer's number is greater or lower than the person's number.


code: 

play_game = True

while play_game:
    import random
    random_number = random.randint(0,100) #change your range here
    print ('\n\nHello, welcome to the number generator.\nWhat number do you think I chose? Come on, I will give you a tip, go from 1 to 100...\n') #dont forget to change your clue here if you change the range
    person_number = int(input ("Write the number here: "))
    if random_number == person_number:
            print("Well done, you got it right!")
            play_again = input("Do you want to play again? Write 'yes' if would like to play again or 'no' if you wouldnt like: ")
            if play_again == "yes":
                exec(open("c:/Users/Administrador/.vscode/code/jogo2.py").read()) #insert your file path here
            else:
                print ('Thanks for playing, hope you enjoyed it :)')
                break
        
    elif random_number < person_number:
            print("The number is lower than "+ str(person_number))

            play_game2 = True

            while play_game2: 
                person_number2 = int(input ("Try again. Write here the number: "))
                if random_number == person_number2:
                    print("Well done, you got it right!")
                    play_again = input("Do you want to play again? Write 'yes' if would like to play again or 'no' if you wouldnt like: ")
                    if  play_again == "yes":
                        exec(open("c:/Users/Administrador/.vscode/code/jogo2.py").read()) #insert your file path here
                    else:
                        print ('Thanks for playing, hope you enjoyed it :)')
                        break
                elif random_number < person_number2:
                    print("The number is lower than "+ str(person_number2))
                    play_game2 = True
                    while play_game2: 
                        person_number2 = int(input ("Try again. Write here the number: "))
                        if random_number == person_number2:
                            print("Well done, you got it right!")
                            play_again = input("Do you want to play again? Write 'yes' if would like to play again or 'no' if you wouldnt like: ")
                            if  play_again == "yes":
                                exec(open("c:/Users/Administrador/.vscode/code/jogo2.py").read()) #insert your file path here
                            else:
                                print ('Thanks for playing, hope you enjoyed it :)')
                                break
                        elif random_number < person_number2:
                            print ("The number is lower than " + str(person_number2))
                            play_game2 = True
                        else:
                            print("The number is greater than " + str(person_number2))
                            play_game2 = True
                else:
                    print ("The number is greater than " + str(person_number2))
                    play_game2 = True
    else:
            print("The number is greater than "+ str(person_number))
            play_game2 = True
            while play_game2: 
                person_number2 = int(input ("Try again. Write here the number:  "))
                if random_number == person_number2:
                        print("Well done, you got it right!")
                        play_again = input("Do you want to play again? Write 'yes' if would like to play again or 'no' if you wouldnt like: ")
                        if  play_again == "yes":
                            exec(open("c:/Users/Administrador/.vscode/code/jogo2.py").read()) #insert your file path here
                        else:
                            print ('Thanks for playing, hope you enjoyed it :)')
                            break
                elif random_number < person_number2:
                    print("The number is lower than "+ str(person_number2))
                    play_game2 = True
                    while play_game2: 
                        person_number2 = int(input ("Try again. Write here the number: "))
                        if random_number == person_number2:
                                print("Well done, you got it right!")
                                play_again = input("Do you want to play again? Write 'yes' if would like to play again or 'no' if you wouldnt like: ")
                                if  play_again == "yes":
                                    exec(open("c:/Users/Administrador/.vscode/code/jogo2.py").read()) #insert your file path here
                                else:
                                    print ('Thanks for playing, hope you enjoyed it :)')
                                    break
                        elif random_number < person_number2:
                                print ("The number is lower than " + str(person_number2))
                                play_game2 = True
                        else:
                                print("The number is greater than " + str(person_number2))
                                play_game2 = True
                else:
                    print ("The number is greater than " + str(person_number2))
                    play_game2 = True
