print(".....Rock.....")
print(".....Paper.....")
print(".....Scissors.....")

player_1=input("Player 1 , Make your input : ")
player_2=input("Player 2 , Make your input : ")

if player_1 =='Rock' and player_2 =='Scissors':
    print("Player 1 wins !!")
elif player_1 =='Rock' and player_2 =='Paper':
    print("Player 2 wins !!")
elif player_1 =='Scissors' and player_2 =='Paper':
    print("Player 1 wins !!")
elif player_1 =='Scissors' and player_2 =='Rock':
    print("Player 2 wins !!")
elif player_1 =='Paper' and player_2 =='Rock':
    print("Player 1 wins !!")
elif player_1 =='Paper' and player_2 =='Scissors':
    print("Player 2 wins !!")
elif player_1 == player_2:
    print(" Game is a Tie !! ")
else:
    print("Something went wrong  !!!!")

