#-------------program for inventary management------------#

print("Today's menu")
menu = {'apple':40,'banana':35,'mango':40,'watermelon':50}
print(menu)
money = int(input('Enter amount you want to add to your card: '))
cart={}
print('Choose item and amount you want')
choose = 'yes'

#--------------------to add item in cart-----------------------#

while(choose != 'no'):
    item_name = input('Enter name of fruit you want: ').lower()
    quantity = int(input('How much do you want? :'))
    if item_name in menu:
        cart[item_name] = quantity
        money = money - (menu[item_name]*quantity)
    choose=input('Do you want to continue?(yes/no):').lower()


#---------------------to remove  item from the cart---------------------------#

def remove_item():
    item_name = input('Enter name of fruit you want to remove: ').lower()
    if item_name in cart:
        quantity = int(input('How much do you want to remove? :'))
        if quantity <= cart[item_name]:
            cart[item_name] -= quantity
            money += menu[item_name]*quantity
        else:
            print("You don't have that much quantity in your cart.")
    else:
        print("Item not found in your cart.")

remove = input('Do you want to remove any item from your cart?(yes/no):').lower()
if remove == 'yes':
    remove_item()

#---------------remaining balance-------------------#    

print('Your remaining balance is ',money)
if(money<0):
    print('Not sufficient balance.')
else:
    print('Items added to your cart\n',cart)
print('Thank you for shopping. See you again.\n')
