import random

print("WELCOME TO ROCK ,PAPER,SCISSORS")
print('Lets get to the rules of the game so that you can play the game without no confusion.')
print("Winning rules are as follows")
print('1. ROCK  Vs PAPER   the winner is ROCK.')
print('2. ROCK  Vs SCISSOR the winner is ROCK.')
print('3. PAPER Vs SCISSOR the winner is SCISSOR.')

while True:
    print(' enter your choice 
        1. ROCK
        2. PAPER
        3. SCISSOR')
    choice= int(input(' User turn : enter your choice'))
    if choice > 3 or choice < 1 :
        print('invalid input please enter your choice as 1,2 or 3.')
    if choice ==1:
        user choice= 'ROCK'
    elif choice == 2:
        user choice= 'PAPER'
    else:
        user choice= 'SCISSOR'
     print(" Now its computer's turn ")
     computer choice = random.randint(1,3)

    while computer choice == choice:
        computer choice = random.randint(1,3)
    if computer choice= 1:
        comp choice name= 'ROCK'
    elif computer choice = 2:
        comp choice name = 'PAPER'
    elif computer choice =3:
        comp choice name = 'SCISSOR'

    print('Computers choice is,' computer choice)
    print(user choice'Vs' computer choice name)

    if user choice= computer choice:
         print('Both players selected same object its a TIE!')
    if user choice='1'  and computer choice ='3' :
        print('RESULT : ROCK WINS !!! CONGRATS USER YOU HAVE WON')
    elif user choice ='2' and computer choice  ='3':
        print('RESULT: SCISSOR WINS!! SORRY USER COMPUTER HAVE DEFEATED YOU BETTER LUCK NEXT TIME ')
    elif user choice ='1' and computer choice  ='2':
        print('RESULT : PAPER WINS !!!  SORRY USER  COMPUTER HAVE DEAFETD YOUBETTER LUCK NEXT TIME')
    elif user choice ='2' and computer choice ='1':
        print('RESULT : PAPER WINS!!! CONGARTS USER YOU HAVE WON ') 
    elif user choice ='3' and computer choice ='1':
        print('ROCK WINS!!! SORRY USER COMPUTER HAVE DEFEATED YOU BETTER LUCK NEXT TIME')
    elif user choice= '3' and computer choice ='2':
        print('RESULT: SCISSOR WINS!!! CONGRATS USER YOU HAVE WON')

    print('Do you want to play again ? Y/N')
    ans=input()
    if ans== 'N'or ans=='n':
        break
print('Thanks for playing the game')
print('Game created by Aparna')
