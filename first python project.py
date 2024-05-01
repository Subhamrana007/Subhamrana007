import random

user_wins = 0
computer_wins = 0

options =  ["rock", "paper", "scissor"]
while True:
    user_input = input("Type rock/papers/scissors or q to quit.").lower()
    if user_input == "q":
        break;

    if user_input not in options: 
        continue

    
    random_number = random.randint(0, 2)
    # in this program 0 stands for rock and 1 for paper and 2 for scissors.

    computer_pick = options[random_number]
    print("computer picked:" , computer_pick)

    if user_input == "rock" and computer_pick == "paper":
        print("you lost")
        computer_wins +=1
        
    elif user_input == "paper" and computer_pick == "scissor":
        print("you lost")
        computer_wins +=1
        
    elif user_input == "scissor" and computer_pick == "rock":
        print("you lost")
        computer_wins +=1
        
    
    else:
        print("you won!")
        user_wins +=1


print("you won", user_wins, "times")
print("the computer wins", computer_wins, "times")
print("GOODBYE! HOWEVER IF YOU WOULD LIKE TO PLAY AGAIN JUST COME BY")


