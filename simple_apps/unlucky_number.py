for i in range (1,21):
    if i ==4 or i ==13:
        state='Unlucky'
    elif i %2 ==1:
        state='Odd'
    else :
        state='Even'
    print(f'{i} is {state}')

