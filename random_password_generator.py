
from password_character_selection import all_options, special_characters, alphabet_lower, all_caps, numbers

import random

import re

def parameters_for_random_password(number):
    n = int(number)
    if n == 0:
        exit('INVALID ENTRY! Please enter a number greater than 0')
    elif n >= 8 and n <= 20:
        input('Your password will have ' + str(n) + ' characters.')
        return True
    elif 1 <= n <= 7:
        exit('INVALID ENTRY! Please enter a number greater than 7 and less than or equal to 20.')
    elif n >= 21:
        exit('INVALID ENTRY! Please enter a number greater than 7 and less than or equal to 20.')
    elif n <= -1:
        exit('INVALID ENTRY! Please enter a positive number.')
    else:
        exit('Please enter a valid number.')

def number_count_for_custom_password(password):
    p = str(password)
    lcount = dcount = spcount = 0
    for i in p:
        if i.isdigit():
            dcount += 1
        elif i.isalpha():
            lcount += 1
        else:
            spcount += 1

    return lcount + dcount + spcount


def parameters_for_custom_password(password):
    user_custom_password = password
    total_number_check = number_count_for_custom_password(password)
    spec_char_check = re.compile(special_characters)
    lower_case_check = re.compile(alphabet_lower)
    upper_case_check = re.compile(all_caps)
    number_check = re.compile(numbers)
    if total_number_check <= 8:
        print('INVALID entry! Your password must be longer than 8 characters. Please try again.')
    elif spec_char_check.search(user_custom_password) == None:
        print('INVALID entry! You password must contain at least one special character. Please try again')
    elif lower_case_check.search(user_custom_password) == None:
        print('INVALID entry! Your password must contain at least one lower case letter. Please try again.')
    elif upper_case_check.search(user_custom_password) == None:
        print('INVALID entry! Your password must contain at least one upper case letter. Please try again.')
    elif number_check.search(user_custom_password) == None:
        print('INVALID entry! Your password must contain at least a number. Please try again.')




def translate(password_as_list):
    translation = ''
    for under_score in password_as_list:
        if under_score in '_':
            translation = translation + random.choice(all_options)



    return translation




def random_password_save(answer):
    user_answer = answer
    if user_answer == 'S' or 'K':
        print('\nOk. Your password \'' + user_password_random + '\' has been saved. ')
    elif user_answer == 'D':
        print('\nOk. Type your new password below.')
    else:
        exit('ERROR! Invalid input!')

def custom_password_save(answer):
    user_answer = answer
    if user_answer == 'S' or 'K':
        print('\nOk. Your password (not including the brackets) [' + custom_made_password + '] has been saved. ')
    elif user_answer == 'D':
        print('\nOk. Type your new password below.')
    else:
        exit('ERROR! Invalid input!')

question_one = int(input('How many elements/characters do you want in your passsword?  '
                  'Enter a number: '))

parameters_for_random_password(question_one)


empty_entry = '_'
length_as_list = []
n = int(question_one)

for i in range(n):
    length_as_list.append(empty_entry)


done = False



while not done:
    user_password_random = (translate(length_as_list))
    potential_password = print('\nHere\'s your randomly generated password: ' + '\n' + str(user_password_random) )
    keep_reject_custom = input('\nWould you like to keep and save this password, generate a new one, or create your own.'
                           '\n(TYPE \'K\' to keep or \'G\' to generate a new one or \'C\' to create your own.'
                           '\nANSWER: ').upper()
    if keep_reject_custom == 'K':
        random_password_save(keep_reject_custom)
        exit()
    elif keep_reject_custom == 'G':
        print('\nYou chose to generate a new random password.')
        done = False
    elif keep_reject_custom == 'C':
        print('OK, create your password below.')
        break
    else:
        exit('INVALID input.')


print('')
custom_made_password = str(input('Password: '))
parameters_for_custom_password(custom_made_password)



while not done:
    your_custom_made_password = input('\nYour password is: \n' + str(custom_made_password) +
                                      '\nWould you like to save your'
                                    ' custom made password? Or discard to type a new password?'
                                    '\n(TYPE S to save it or TYPE D to discard it to type a new password.)'
                                    '\nANSWER: ').upper()
    if your_custom_made_password == 'S':
        custom_password_save(custom_made_password)
        break
    elif your_custom_made_password == 'D':
        print('\nOk. Type in your password below.')
        done = False
    else:
        print('INVALID input! Re-type your desired password.')






