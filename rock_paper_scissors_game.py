import random
data=['rock','paper','scissors']

while True:
    user_input=input("enter your input from (rock,paper,scissors)")
    computer_user=random.choice(data)
    
    if user_input == computer_user:
        print("GAME TIE!")
    
    elif user_input == 'paper':
        if computer_user=='rock':
            print('User won the game')
        
        else:
            printf('computer won the game')
    
    elif user_input == 'rock':
        if computer_user=='paper':
            print('computer won the game')
            
        else:
            print('User won  the game')
    
    else:
        if computer_user == 'rock':
            print('computer won the game')
            
        else:
            print('User won the game')
            
    user=input('if you want to continue press y')
    
    if user.lower()!='y':
        break
        
