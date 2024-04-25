print("today's menu")
menu = {'apple':'40/kg','banana':'35/kg','mango':'40/kg','watermeleon':'50/kg'}
print(menu)
money = int(input('enter amount you want to add to your card: '))
cart={}
print('choose item and amount you want')
choose = 'yes'
while(choose != 'no'):
    item_name = input('enter name of fruit you want: ').lower()
    quantity = int(input('how much do you want? :'))
    cart[item_name] = quantity
    choose=input('do you want to continue?(yes/no):').lower()
while(money != 0):
    if item_name == 'apple':
        cart['apple'] = 40*quantity
    elif item_name == 'banana':
        cart['banana'] = 35*quantity
    elif item_name ==  'mango':
        cart['mango'] = 40*quantity
    elif item_name == 'watermelon':
        cart['watermeleon'] = 50*quantity
    money = money-(cart[item_name])
print('your remaining balance is ',money)
if(money<0):
    print('not sufficent balance.')
else:
    print('items added to your cart\n',cart)
print('thankyou for shopping. see you again.\n')
