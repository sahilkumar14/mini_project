y = 0
par01 = 0
par02 = 0
par03 = 0
par04 = 0
par05 = 0

while(y<=3):
    name = input('enter your name: ')
    age = int(input("Enter your age: "))

    if age >= 18:
      print('your are eligible to vote.')
    else:
        print('you are not eligible to vote')
        break

#-------------list of parties----------------#

    print('select your party to vote>')
    print('party-01')
    print('party-02')
    print('party-03')
    print('party-04')
    print('party-05')
    vote = int(input('choose your party to vote(1/2/3/4/5): '))
    if vote == 1 :
        par01 += 1
    elif vote == 2 :
        par02 += 1
    elif  vote == 3 :
        par03 += 1
    elif  vote == 4 :
        par04 += 1
    else:
        par05 += 1
    print('thankyou for voting.\n')
    y = y+1
print(f'party-01 got {par01} votes.\n')
print(f'party-02 got {par02} votes.\n')
print(f'party-03 got  {par03} votes.\n')
print(f'party-04 got  {par04} votes.\n')
print(f'party-05 got  {par05} votes.\n')

