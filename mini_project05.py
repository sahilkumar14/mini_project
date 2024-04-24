import random
y = 'yes'
while (y != 'no'):
    dice = random.randint(1,6)
    print(dice)
    y = input("Do you want to roll again? Type yes or no: ".lower())
print('happy rolling')