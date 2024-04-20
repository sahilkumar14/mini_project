y = 'yes'
while(y!='no'):
    try:
        num = int(input('enter number system range: '))
    except Exception:
        print('please enter vaild number.')
    else:
        print('how you want your number system to display?')
        print('1.forward way')
        print('2.backward way')
        choice = int(input('enter your choice number: '))
        print('how you want them to display?')
        print('1.row wise')
        print('2.column wise')
        c_choice = int(input('enter your choice number: '))
        if choice == 1:
            if c_choice == 1:
                for i in range(1,num):
                    print(i,end=',')
            elif c_choice == 2:
                for i in range(1,num):
                    print(i)
        if choice == 2:
            if  c_choice == 1:
                for j in range(num,0,-1):
                    print(j, end=",")
            elif c_choice == 2:
                for j in range(num,0, -1):
                    print(j)

    print('\n')           
    y = input('want to continue with new set of numbers(yes/no)?:'.lower())
print('here is your format of number!!!!.')

