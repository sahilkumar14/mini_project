import random
user_win = 0
computer_win = 0
choose = 'yes'
while (choose != 'no'):
    li = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(li)
    print("You can choose rock, paper or scissors: ",end='')
    user_choice = input().lower()
    if user_choice == computer_choice:
      print('It is a tie!')

#----------------rock---------------#
    elif (user_choice == 'rock' and computer_choice == 'scissors'):
      print('computer win!!')
      computer_win += 1

    elif (user_choice == 'rock' and computer_choice == 'paper'):
      print('you win!!')
      user_win += 1

#----------------paper---------------#
    elif (user_choice == 'paper' and computer_choice ==  'rock'):
      print('You Win!!')
      user_win += 1

    elif (user_choice == 'paper' and computer_choice == 'scissors'):
      print('computer wins!!')
      computer_win += 1

#----------------scissors-------------#
    elif(user_choice == 'scissors' and computer_choice == 'rock'):
      print('computer wins!!')
      computer_win+=1

    elif (user_choice == 'scissors' and computer_choice == 'paper'):
      print('you win!!')
      user_win+=1

    choose = input('want to play again: ').lower()
print(f'you total win is: {user_win}')
print(f'computer total win is: {computer_win}')