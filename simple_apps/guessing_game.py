from random import randint 

random_num=randint(1,100)
user_num=None


while True:
    user_num=int(input("Please guess a number between 1 & 100 !!"))

    if user_num > random_num:
        print("Oh ! Too high ")
    elif user_num < random_num: 
        print(" oh ! Too Low ")
    else :
        print("Yay you guessed it right this time !! ")
        game=input("Do you want to play again  ? (y/n) ")
        if game =='y':
            random_num=randint(1,100)
            user_num=None
        else:
            print("Thanks for playing !!")
            break

