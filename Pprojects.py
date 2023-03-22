#Rock Paper Scissor Game

import random

l1 = ["Rock", "Paper", "Scissors"]   #a list is created so that the computer can take its choice from this

c_choice = random.choice(l1)    #using the random() method the computer gives random choices from the list
h_choice = input("Enter your choice! [Rock Paper Scissors ] ")

print(f"Your choice is : = {h_choice}  and  c_choice = {c_choice}")

if c_choice == h_choice: #checking whether both the choices are same
    print("It's a tie")


elif h_choice == "Scissors":
    if c_choice == "Paper":
        print("You win!")

    else:
        print("Computer wins!")


elif h_choice == "Rock":
    if c_choice == "Scissors":
        print("You win!")

    else:
        print("Computer wins!")


elif h_choice == "Paper":
    if c_choice == "Rock":
        print("You win!")

    else:
        print("Computer wins!")


