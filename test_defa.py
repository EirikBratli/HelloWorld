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

run from terminal: >> python test2_oppg.py

"""

import numpy as np

txt = '''"08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08\n"
"49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00\n"
"81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65\n"
"52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91\n"
"22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80\n"
"24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50\n"
"32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70\n"
"67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21\n"
"24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72\n"
"21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95\n"
"78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92\n"
"16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57\n"
"86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58\n"
"19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40\n"
"04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66\n"
"88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69\n"
"04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36\n"
"20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16\n"
"20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54\n"
"01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48"'''


def sort_txt(txt, N=20):
    """
    Transform the text string into a more appropriate format, a 2D array.

    Input:
    - txt, string. The text string to work with.
    - N, integer.  The number of rows/columns in the text string.

    Return.
    - 2D array with the numbers in the text string as integers.
    """

    txt_list = txt.split(' ')
    store_list = []
    for element in txt_list:
        # extract the numbers
        if (element[0] == '"'):
            store_list.append(element[1:])

        elif (element[-1] == '"'):
            store_list.append(element[:-1])

        elif len(element) > 3:
            store_list.append(element[:2])
            store_list.append(element[-2:])

        else:
            store_list.append(element)

    # Convert from list to array
    store_array = np.asarray(store_list, dtype=int)
    return(np.reshape(store_array, (N, N)))




class MaximumProduct():
    """
    Calculate the maximum value of four values next to each other.

    Input:
    - data, 2D array. The cinverted text string.
    """

    def __init__(self, data):
        self.x = data
        self.res_max = -1
        self.result = {'Max': self.res_max, 'Values': None}
        self.N = len(self.x[0,:])

    def max_product(self):
        """
        Find the highest product of the different cases and print the maximum
        product and the numbers producing the result.
        """

        Max_values = [self.calculate('column')['Max'], \
                    self.calculate('row')['Max'],\
                    self.calculate('diagonal')['Max'],\
                    self.calculate('anti-diagonal')['Max']]

        Max_numbers = [self.calculate('column')['Values'], \
                    self.calculate('row')['Values'],\
                    self.calculate('diagonal')['Values'],\
                    self.calculate('anti-diagonal')['Values']]

        print('=======================')
        print('')
        print('The highest product of four 2 digit numbers next to each other is:')
        print(np.max(Max_values))
        print('With the numbers:')
        print(Max_numbers[np.where(Max_values == np.max(Max_values))[0][0]])
        print('')
        print('=======================')

    def product(self, x):
        """
        Calculate the product of the four numbers next to each other.

        Input:
        - x, sequence. List with the 4 numbers to be multiplied together.

        Return:
        - res, scalar. The product of the four numbers.
        """
        res = x[0] # get an inital value
        for i in range(1,4):
            res *= x[i]
        return(res)

    def get_max(self, res, res_max):
        """
        Find if the product of the current numbers are larger than the current
        maximum product. Else, keep the current maximum value.

        Input:
        - res, scalar.     The product of the current numbers.
        - res_max, scalar. The current maximum value.

        Return:
        - max_res, scalar. The maximum value
        - update, bool.    True max_res is updated, else returns False.
        """

        if res >= res_max:
            res_max = res
            update = True
        else:
            res_max = res_max
            update = False
        return(res_max, update)

    def diagonal(self, x, res_max, name):
        """
        Calculate the product along the diagonal/anti-diagonal.

        Input:
        - x, 2d array.     The array with the numbers to be multiplied.
        - res_max, scalar. The inital res_max value (=-1), which is updated.
        - name, string.    Variable checking for multiply along 'diagonal' or
                           'anti-diagonal'.
        Return:
        - result, dict.    The maximum product value and the values giving the
                           result.
        """

        for i in range(self.N-3):
            for j in range(self.N-3):
                if name[0] == 'd':
                    y = [x[i,j], x[i+1,j+1], x[i+2,j+2], x[i+3,j+3]]
                else:
                    y = [x[i+3,j], x[i+2,j+1], x[i+1,j+2], x[i,j+3]]
                res = self.product(y)
                res_max, update = self.get_max(res, res_max)
                if update is True:
                    self.result['Values'] = y
            self.result['Max'] = res_max
        #
        return(self.result)

    def row_col(self, x, res_max, name):
        """
        Calculate the product along the rows or columns.

        Input:
        - x, 2d array.     The array with the numbers to be multiplied.
        - res_max, scalar. The inital res_max value (=-1), which is updated.
        - name, string.    Variable checking for multiply along 'row' or
                           'column'.
        Return:
        - result, dict.    The maximum product value and the values giving the
                           result.
        """

        if name == 'column':
            # If multipy along column, transpose the 2D array: column --> row.
            x = x.T

        for j in range(self.N):
            for i in range(self.N-3):
                res = self.product(x[j,i:i+4])
                res_max, update = self.get_max(res, res_max)
                if update is True:
                    self.result['Values'] = x[j,i:i+4]

            self.result['Max'] = res_max
        #
        return(self.result)

    def calculate(self, name):
        """
        Calculate the products of the four values next to each other.

        Input:
        - name, string. Variable defining if the product is along 'row', 'column',
                        'diagonal' or 'anti-diagonal'.
        Return:
        - result, dict. Dictionary with the maximum product of the numbers and
                        the values producing the result.
        """

        if (name == 'diagonal') or (name == 'anti-diagonal'):
            self.result = self.diagonal(self.x, self.res_max, name)

        else:
            self.result = self.row_col(self.x, self.res_max, name)

        return(self.result)



# Function calls:

data = sort_txt(txt)
print('')
print('The text string converted to 2D array:')
print(data)
print('')

MaximumProduct(data).max_product()
