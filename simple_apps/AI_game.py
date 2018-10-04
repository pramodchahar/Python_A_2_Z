import random

ai_num=random.randint(1,3)
computer=[]
if ai_num == 1:
    computer='rock'
elif ai_num ==2:
    computer="paper"
else:
    computer='scissors'

player_1=input("Player 1 , Make your input : ").lower()
print(f"Computer choses : {computer}")

if player_1 == computer:
    print(" Game is a Tie !! ")

elif player_1 =='rock':
    if computer =='scissors':
        print("Player 1 wins !!")
    elif computer =='paper':
        print("Computer wins !!")

elif player_1 =='scissors':
    if computer =='paper':
        print("Player 1 wins !!")
    elif computer =='rock':
        print("Computer wins !!")

elif player_1 =='paper':
    if computer =='rock':
        print("Player 1 wins !!")
    elif computer =='scissors':
        print("Computer wins !!")
else:
    print("Something went wrong  !!!!")

