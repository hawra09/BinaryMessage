def binarymessage():
    try:
        user_input = int(input('Please input an integer number greater than 0:'))
        if user_input < 0:
            print('Please input a positive integer!')
        elif user_input == 0:
            print('Please input an integer greater than 0.')
        else:
            while user_input > 0:
                user_input = user_input >> 1
                print(user_input)
    except ValueError:
        print('Invalid input please use a valid integer number.')


binarymessage()

'''
Possible Test Cases Include: 
1. user_input = 0                           Expected Behavior: 'Please input an integer greater than 0.'
2. user_input < 0                           Expected Behavior: 'Please input a positive integer!'
3. user_input = float                       Expected Behavior: 'Invalid input please use a valid integer number.'
4. user_input = str (like 'abc')            Expected Behavior: 'Invalid input please use a valid integer number.'
5. user_input = odd integer                 Expected Behavior: Works properly, shifts right until 0 is reached.
6. user_input = even integer                Expected Behavior: Works properly, shifts right until 0 is reached.
7. user_input = prime integer               Expected Behavior: Works properly, shifts right until 0 is reached.
8. user_input = very large number           Expected Behavior: Works properly, shifts right until 0 is reached.
'''