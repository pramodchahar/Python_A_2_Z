print(".....Rock.....")
print(".....Paper.....")
print(".....Scissors.....")

player_1=input("Player 1 , Make your input : ")

print("*****No Cheating || \n" * 20)
player_2=input("Player 2 , Make your input : ")



if player_1 == player_2:
    print(" Game is a Tie !! ")

elif player_1 =='Rock':
    if player_2 =='Scissors':
        print("Player 1 wins !!")
    elif player_2 =='Paper':
        print("Player 2 wins !!")

elif player_1 =='Scissors':
    if player_2 =='Paper':
        print("Player 1 wins !!")
    elif player_2 =='Rock':
        print("Player 2 wins !!")

elif player_1 =='Paper':
    if player_2 =='Rock':
        print("Player 1 wins !!")
    elif player_2 =='Scissors':
        print("Player 2 wins !!")
else:
    print("Something went wrong  !!!!")

