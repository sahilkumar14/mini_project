print("Today's menu")
menu = {'apple':'40/kg','banana':'35/kg','mango':'40/kg','watermelon':'50/kg'}
print(menu)
money = int(input('Enter amount you want to add to your card: '))
cart={}
print('Choose item and amount you want')

#---------------section for adding items-----------------#

choose = 'yes'
while(choose != 'no'):
    item_name = input('Enter name of fruit you want: ').lower()
    quantity = int(input('How much do you want? :'))
    if item_name == 'apple':
        cart['apple'] = 40*quantity
    elif item_name == 'banana':
        cart['banana'] = 35*quantity
    elif item_name ==  'mango':
        cart['mango'] = 40*quantity
    elif item_name == 'watermelon':
        cart['watermelon'] = 50*quantity
    money = money-(cart[item_name])
    choose=input('Do you want to continue?(yes/no):').lower()

#--------------------tell about remaining money--------------#

print('Your remaining balance is ',money)
if(money<0):
    print('Not sufficient balance.')
else:
    print('Items added to your cart\n',cart)
print('Thank you for shopping. See you again.\n')
