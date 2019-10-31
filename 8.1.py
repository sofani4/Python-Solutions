# reverse list order
def freverse_list_order(arr):
    return arr[::-1]


# altERnaTIng cAsE <=> ALTerNAtiNG CaSe
#Each lowercase letter becomes uppercase,
#and each lowercase letter becomes lowercase
def to_alternating_case(string):
    return string.swapcase()


# Filter the list of strings and return a list with strings whose length = 4
def length_four(x):
    return [i for i in x if len(i) == 4]


#substring search
#Test.assert_equals(is_lock_ness_monster("Your total comes to tree fiddy"), True)
#Test.assert_equals(is_lock_ness_monster("Hello, I come from the year 3150 to bring you good news!"),False)
import re
def is_lock_ness_monster(string):
    return bool(re.search(r"3\.50|tree fiddy|three fifty", string))


# Splitting strings and converting it to a list
# Test.assert_equals(string_to_array("Robin Singh"), ["Robin", "Singh"])
def string_to_array(s):
    return s.split(' ')


# Finding a specific value from the end of an array
#test.assert_equals(warn_the_sheep(['sheep', 'wolf', 'sheep']), 'Oi! Sheep number 1! You are about to be eaten by a wolf!')
#test.assert_equals(warn_the_sheep(['sheep', 'sheep', 'wolf']), 'Pls go away and stop eating my sheep')
def warn_the_sheep(queue):
    if queue.index('wolf')+1 == len(queue):
        return 'Pls go away and stop eating my sheep'
    else:
        serial_number = str((len(queue) - (queue.index('wolf')+1)))
        return 'Oi! Sheep number ' + serial_number + '! You are about to be eaten by a wolf!'


# convert the sum of two decimal numbers to binary representation
def add_binary(a, b):
    return str(bin(a + b))[2:]
