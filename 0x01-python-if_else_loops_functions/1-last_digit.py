#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = abs(number) % 10

if number < 0:
    last_digit = -last_digit

output =  'Last digit of {} and is {} and is '.format(number, last_digit);
if last_digit > 5:
    output += 'greater than 5'
    print(output)
elif last_digit == 0:
    output += '0'
    print(output)
else:
    output += 'than 6 and not 0'
    print(output)
