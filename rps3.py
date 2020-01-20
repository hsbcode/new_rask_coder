import random
print("Welcome to a new Rock Paper Scissors Game.")
y = False
while y == False:
    print("Please choose between rock, paper, and scissors.")
    turn = 0
    player_score = 0
    choice1 = None
    while turn < 5:
        while choice1 != "rock" and choice1 != "paper" and choice1 != "scissors":
            print(f"Turn {turn + 1}:")
            print("Please make your move.")
            choice1 = input()
            choice1 = choice1.lower()
            compchoise = random.randint(0, 2)
            if choice1 != "rock" and choice1 != "paper" and choice1 != "scissors":
                print("You must choose between 'rock', 'paper' and 'scissors'.")
        if compchoise == 0:
            choice2 = "rock"
        elif compchoise == 1:
            choice2 = "paper"
        elif compchoise == 2:
            choice2 = "scissors"
        if choice1 == "rock" or choice1 == "paper" or choice1 == "scissors":
            print("The computer said " + choice2 + ".")
            if choice1 == "rock" and choice2 == "rock":
                print("It was a tie.")
            elif choice1 == "rock" and choice2 == "paper":
                print("The computer wins.")
            elif choice1 == "rock" and choice2 == "scissors":
                print("You win. Congratulations!")
                player_score += 1
            elif choice1 == "paper" and choice2 == "scissors":
                print("Computer wins.")
            elif choice1 == "paper" and choice2 == "paper":
                print("It was a tie.")
            elif choice1 == "paper" and choice2 == "rock":
                print("You win. Congratulations!")
                player_score += 1
            elif choice1 == "scissors" and choice2 == "scissors":
                print("It was a tie.")
            elif choice1 == "scissors" and choice2 == "paper":
                print("You win. Congratulations!")
                player_score += 1
            elif choice1 == "scissors" and choice2 == "rock":
                print("Computer wins.")
        choice1 = None
        turn += 1
    print(f"Game over. You got {player_score} out of 5 points.")
    if player_score == 0:
        print("You suck at this game. Don't you?")
    elif player_score == 1:
        print("Well, better than nothing.")
    elif player_score == 2:
        print("Could be better.")
    elif player_score == 3:
        print("Not bad!")
    elif player_score == 4:
        print("Nice!")
    elif player_score == 5:
        print("Wow! Well done!")
    t = False
    while t == False:
        replay = input("Do you wanna play again?(y/n): ")
        if replay == "y" or replay == "Y":
            t = True
        elif replay == "n" or replay == "N":
            t = True
            y = True
            print("Thanks for playing!")
        else:
            print("Please type in a valid answer.")
