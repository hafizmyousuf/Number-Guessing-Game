import random


easy = 100
medium = 500
hard = 2000

user = input("Please choose your difficulty level: \n\tEasy \n\tMedium \n\tHard \n")
if user == "easy" or user == "Easy":
    uservalue = easy
elif user == "medium" or user == "Medium":
    uservalue = medium
elif user == "hard" or user == "Hard":
    uservalue = hard
else:
    print("Invalid action")

def number_guessing_game():
    bot_guess = random.randint(1,uservalue)
    attempts =0


    while True:

        guess = int(input("Enter your Guess: "))
        
        attempts +=1
        
        if guess > bot_guess:
            print("The number you guess is High. Enter another number ")
        elif guess< bot_guess:
            print("The number you guess is low. Enter another number ")
        else:
            print(f"Congratulation! You guess right number in {attempts} attempts")

            play_again = (input("If you want to play again press y/n and hit the button ENTER: "))
            if play_again == "y" or play_again == "Y":
                number_guessing_game()
            else:
                print("Game succesfully closed")
            break

            
            
number_guessing_game()