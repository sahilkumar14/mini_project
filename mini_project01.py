y = 'yes'
while(y != 'no'):

#----------to check if input is correct or not----------#

    try:
      num1 = eval(input('enter first number: '))
      num2 = eval(input('enter second number: '))
    except Exception:
      print('enter only numeric value.')

#--------section for choosing operation----------#

    else:
      print('choose your operation to perform(1/2/3/4):')
      print("1.Addition")
      print("2.Subtraction")
      print("3.Multiplication")
      print('4.division')

#-------section for making choice--------#

    choice = int(input())
    if choice == 1:
      print(f'the sum of {num1} and {num2} is {num1+num2}')
    elif choice == 2:
      if num2 > num1:
        print(f"{num1}   is subtracted from {num2}, the result is {num2-num1}")
      else:
        print(f'{num2} is subtracted from {num1}, the result is {num1-num2}')
    elif choice == 3:
       print(f'The product of {num1} and {num2} is {num1*num2}')
    elif choice == 4:
      try:
        res=num1/num2
      except Exception:
        print('please enter valid input.')
      else:
        print(f'{num1} divided by {num2} is {res}')

#-----------choice for continuing calculation------------#

    y = input('want to calculate again?(yes/no):'.lower())
print('calculation done!')
