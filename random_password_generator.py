
from password_character_selection import all_options, special_characters, alphabet_lower, all_caps, numbers

import random

errors_ = []

def custom_password_error_check(password):
    user_password = password

    if not any(c.islower() for c in user_password):
        errors_.append("\n*Your password must contain at least one lower case letter.")
    if not any(c.isupper() for c in user_password):
        errors_.append("\n*Your password must contain at least one upper case letter.")
    if not any(c.isdigit() for c in user_password):
        errors_.append("\n*Your password must contain at least one digit.")
    if len(user_password) < 7:
        errors_.append("\n*Your password must contain at least eight characters.")
    if not any([x in user_password for x in "~!@#$%^&*_+=-?><|"]):
        errors_.append("\n*Your password must contain at least one special character.")
    errors_.append(try_again)
    errors_.insert(0, errors_intro)
    if len(errors_) >= 3:
        print(''.join(errors_) )
        input('(Press ENTER to continue.)')
        errors_.clear()
    elif len(errors_) <= 2:
        return True


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

custom_made_password = str('')

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
                           '\n(TYPE \'K\' to keep or \'G\' to generate a new one or \'C\' to create your own.)'
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

try_again = '\nPlease try again.'
errors_intro = '\nYour password is missing the following: '

done = False


done_two = False











condition = 0



while not done:
    print('\n(Password\'s parameters:'
          '\n*contain at least one lower case letter.'
          '\n*contain at least one upper case letter.'
          '\n*contain at least one digit.'
          '\n*contain at least one special character.'
          '\n*must be greater than 7 characters and less than 21 characters.)')
    user_password = str(input('\nPassword: '))

    if custom_password_error_check(user_password):
        if len(errors_) >= 3:
            errors_.clear()
            done = False
        elif len(errors_) == 2:
            errors_.clear()
            if any(c.islower() for c in user_password) and any(c.isupper() for c in user_password) and \
            any(c.isdigit() for c in user_password) and len(user_password) >= 8 and \
            any([x in user_password for x in "~!@#$%^&*_+=-?><|"]):
                p_or_c = input('\nYour password has met all of the parameters. Would you like to '
                               'proceed with this password and save it or discard it to create a new one? '
                               '(TYPE P to proceed or C to discard the current password in order to create another. \n ANSWER: ').upper()
                while not done_two:
                    if p_or_c == 'P':
                        print('\nOk.')
                        break
                    elif p_or_c == 'C':
                        print('Ok. Password has been discarded. Create your password below.')
                        condition += 1
                        break
                    else:
                        print('INVALID input! Please enter a valid input. Will now reset to password prompt.')
                        condition += 1
                        break
    if condition == 1:
        condition -= 1

    elif any(c.islower() for c in user_password) and any(c.isupper() for c in user_password) and \
            any(c.isdigit() for c in user_password) and len(user_password) >= 8 and \
            any([x in user_password for x in "~!@#$%^&*_+=-?><|"]):
        done = True


saved_password = user_password
print('Your password: \n' + user_password + '\nhas been saved. ')
