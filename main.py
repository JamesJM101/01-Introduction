#!/usr/bin/env python3

import utils

utils.check_version((3,7))
utils.clear()

ex = ''
while (ex !='7'):
    print('1.My Name')
    print('2.My favorite game')
    print('3.My concerns about the class')
    print("4.What I'm excited about")
    print('5.My Stackoverflow.com user number')
    print('6.My github.com profile url')
    print('7.Exit')
    ex = input('Type the number of the question you would like to ask')
    if (ex == '1'):
        print('A:Hello, My name is James Maxwell')
    elif (ex == '2'):
        print('A:Fallout New Vegas')
    elif (ex == '3'):
        print('A:Time management')
    elif (ex == '4'):
        print('A:Learning new things related to my major')
    elif (ex == '5'):
        print('A:11991285')
    elif (ex == '6'):
        print('https://github.com/JamesJM101')
    elif (ex == '7'):
        print('Goodbye')
    else:
        print('Please select an option from the list')

