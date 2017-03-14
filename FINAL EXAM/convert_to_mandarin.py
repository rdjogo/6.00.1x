#!/usr/bin/python3

def convert_to_mandarin(us_num):
    '''
    us_num, a string representing a US number 0 to 99
    returns the string mandarin representation of us_num
    '''

    trans = {'0':'ling', '1':'yi', '2':'er', '3':'san', '4': 'si',
             '5':'wu', '6':'liu', '7':'qi', '8':'ba', '9':'jiu', '10': 'shi'}

    if len(us_num) == 1:
        return trans[us_num]

    elif int(us_num) == 10:
        return trans['10']

    elif int(us_num) in range(11,20):        
        return trans['10'] + ' ' + trans[str(int(us_num) - 10)]

    elif int(us_num) in range(20,100):
        if int(us_num) % 10 == 0:
            return trans[str(int(us_num)//10)] + ' ' + trans['10']
        else:
            return trans[str(int(us_num)//10)] + ' ' + trans['10'] + ' ' + trans[str(int(us_num)%10)]
    