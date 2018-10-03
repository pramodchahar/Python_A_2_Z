import random

ai_num=random.randint(1,3)
computer=[]
if ai_num == 1:
    computer='Rock'
elif ai_num ==2:
    computer="Paper"
else:
    computer='Scissors'

player_1=input("Player 1 , Make your input : ")
print(f"Computer choses : {computer}")

if player_1 == computer:
    print(" Game is a Tie !! ")

elif player_1 =='Rock':
    if computer =='Scissors':
        print("Player 1 wins !!")
    elif computer =='Paper':
        print("Computer wins !!")

elif player_1 =='Scissors':
    if computer =='Paper':
        print("Player 1 wins !!")
    elif computer =='Rock':
        print("Computer wins !!")

elif player_1 =='Paper':
    if computer =='Rock':
        print("Player 1 wins !!")
    elif computer =='Scissors':
        print("Computer wins !!")
else:
    print("Something went wrong  !!!!")

