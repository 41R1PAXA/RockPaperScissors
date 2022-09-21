import random
turns = ["rock", "paper", "scissors"]

human_turn = input("Your turn is  ")
computer_turn = (random.choice(turns))
print ("Computer turn is " + computer_turn)

print (f'Human: {human_turn} vs. Computer: {computer_turn}')

if human_turn == computer_turn:
    print("DRAW!")

elif human_turn == "rock" and computer_turn == "paper":
    print("Computer wins!")
elif human_turn == "paper" and computer_turn == "scissors":
    print("Computer wins!")
elif human_turn == "scissors" and computer_turn == "rock":
    print("Computer wins!")

else:
    print ("human wins!")
