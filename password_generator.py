import random


def password_generate(length):
    digits =[0,1,2,3,4,5,6,7,8,9]
    lower_char= ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                     'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
                     'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
                     'z']
    upper_char = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                     'I', 'J', 'K', 'M', 'N', 'O', 'p', 'Q',
                     'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
                     'Z']

    symbol = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>','*', '(', ')', '<']
    all_list = lower_char+upper_char+symbol+digits
    pass_1 = random.choice(str(digits))+random.choice(symbol)+random.choice(upper_char)+random.choice(lower_char)

    for i in range(length-4):
        pass_1 = pass_1 + str(random.choice(all_list))
    return pass_1


