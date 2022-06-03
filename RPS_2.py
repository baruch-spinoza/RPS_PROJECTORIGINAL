import random
import sys


while True:
    print('Enter R  ROCK\n Enter P for \nEnter S for SCISSORS\n')
    user_action=str(input('Enter a choice R\n P\n or S: '))
    possible_actions=['R', 'P', 'S']
    
    computer_action=random.choice(possible_actions)
    
    if user_action == computer_action:
        print("Both players  It is a tie!")
    elif user_action == 'R' :
        if computer_action == 'S':
            print('Rock smashes Scissors You win!')        
        else:
              print('You lose paper covers rock')
            
        
    
        
    elif user_action == 'P':
        if computer_action == 'R':
          print('You win, paper covers rock!')
        else:
             print('You lose Scissors Cuts Paper!')
        
     
    elif user_action == 'R':
        if computer_action ==  'P':
          print('You win, Scissors cuts paper!')
         
        else:
            print('You lose Rock smashes Paper!')
            
    else: 
            print('please enter the correct input')
            
    while True:   
        play_1= ['y', 'Y']
        play_2=['n','N']
        play_again= input('Play again? (y/n): ')
        if play_again in play_1:
            print('You have chosen to continue...')
            break
     
        elif play_again  in play_2:
            sys.exit('You have chosen to exit the system')
            
        else:
            print('Enter the correct input\n Y or N')
            
    
      
            
        
       
    else:
        break
           
           
       
        
        
     
        
  