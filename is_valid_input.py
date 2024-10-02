from GlobalVariables import *


def is_valid_input(user_input):
    return all(char in alphabet_list for char in user_input) and user_input.strip()