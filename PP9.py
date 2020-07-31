import random
import re

count = 0
a = random.randint(1,9)
# generates random number between 1 and 9

while True:
    b = input('Enter: ')
# take user input for integer
# he has to guess the number by hit and trial

    if re.findall('^[0-9]*$',b) or re.findall('^[-][0-9]*$',b):
# regular expression for positive and negative numbers
        b = int(b)
        count = count + 1
# counts the number of attempts
    elif b == 'exit':
        break
    else:
        print('Please enter integer')
# prompts for integral value only
        continue

    if b < a:
        print('You entered low number')
    elif b == a:
        print('Entered number matches')
        break
    else:
        print('You entered high number')
# feedbacks

print('You played ', count, 'times.')
# display result
