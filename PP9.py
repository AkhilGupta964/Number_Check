import random
import re

count = 0
a = random.randint(1,9)

while True:
    b = input('Enter: ')

    if re.findall('^[0-9]*$',b) or re.findall('^[-][0-9]*$',b):
        b = int(b)
        count = count + 1
    elif b == 'exit':
        break
    else:
        print('Please enter integer')
        continue

    if b < a:
        print('You entered low number')
    elif b == a:
        print('Entered number matches')
    else:
        print('You entered high number')

print('You played ', count, 'times.')
