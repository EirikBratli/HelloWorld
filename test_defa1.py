"""
This program aims to solve the following task given by Panamera IDM for
recruiting:

'The assignment is as follows:
Below is a variable that contains a text string. Rewrite the syntax to an
appropriate string type for your coding language and parse it as the start of
your solution. Then create an application that prints the highest possible
product you can get from 4 two digit numbers that are next to each other, either
in a row, column or in any of the diagonals (including the anti-diagonals).
For example, the numbers marked with red has the product 1788696, but that is
not the correct answer.'

@ Code written by Eirik Bratli

"""

import numpy as np

"""
Need to load as a string, convert to each number to float, store in 2D array
loop through on row, cols, and diag/anti-diag, and compute max product of 4 digit
next to each other.

check if first digit is 0, e.g. '04' -> '0'+'4'
"""

file = 'num.txt'


#print(txt, len(txt))
def load(file):
    """
    Load the data to be analysed.
    Input: Filename of the .txt file.
    Return: The loaded data as a list containing strings for each line.
    """
    txt = open(file, 'r')
    lines = txt.readlines()
    #print(lines, len(lines))
    return(lines)


def create_2d_array(data):
    """
    Transform the data from list with strings to a 2D array with scalars.
    Input: data, list with the numers as a sequence of strings
    """

    Nrows = len(data)
    dt = []
    for i in range(Nrows):
        line = data[i]
        nums = line.split(' ')

        # strip for characters that are not numbers
        num = not_number(nums)
        #print(len(num))
        dt.append(num)
    #
    return(np.asarray(dt))

def not_number(num):
    """
    strip for characters that are not numbers
    """
    l = []
    for x in num:
        if x[0] == '"':
            x = x[1:]
        elif len(x) > 3:
            x = x[:2]
        # check if first digit is 0:
        #x = is_zero(x)
        l.append(int(x))
        #
    return(l)

def is_zero(x):
    # check if first digit is zero
    if x[0] == '0':
        x = x[1:]
    return(x)

def product(x):
    res = x[0]
    for i in range(1,4):
        res *= x[i]
        #print(i,res, x[:i])
    return(res)

def get_max(res, res_max):
    if res >= res_max:
        res_max = res
    else:
        pass
    return(res_max)

def diagonal(x, N, result, res_max, name):
    """
    Calculate the product along the diagonal/anti-diagonal
    """
    for i in range(N-3):
        for j in range(N-3):
            if name[0] == 'd':
                y = [x[i,j], x[i+1,j+1], x[i+2,j+2], x[i+3,j+3]]
            else:
                y = [x[i+3,j], x[i+2,j+1], x[i+1,j+2], x[i,j+3]]
            res = product(y)
            res_max = get_max(res, res_max)
            #print(i, j, y, res, res_max) # 9, 16
        #break
        result['Max'] = res_max
    #
    #print(result)
    return(result)

def Calculate_product(x, res_max=-1, name='Row'):
    """
    Calculate the product along the rows.
    """
    N = len(x[0,:])
    result = {'Max': res_max}
    print('Calculate product along'+ name)
    if (name == 'diagonal') or (name == 'anti-diagonal'):
        # run for diagonal:
        result = diagonal(x, N, result, res_max, name)

    else:
        if name == 'column':
            x = x.T
        #
        for j in range(N):
            #print(name, j)
            for i in range(N-3):
                res = product(x[j,i:i+4])
                #print(res, x[j,i:i+4])
                res_max = get_max(res, res_max)
                #if res >= res_max:
                #    res_max = res
                #else:
                #    pass
            result['Max'] = res_max

    print(result)
    return(result)
######################################

#Function calls:

txtdata = load(file)
data = create_2d_array(txtdata)


print(data[:,:10])
print(data[:,10:])
# Do calculations
max_row = Calculate_product(data)
max_col = Calculate_product(data, name='column')
max_diag = Calculate_product(data, name='diagonal')
max_anti = Calculate_product(data, name='anti-diagonal')


#
