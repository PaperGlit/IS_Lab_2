import math
from GlobalVariables import *


def coder(text, key, decode = False):
    key = (key * math.ceil(len(text) / len(key)))[:len(text)]
    result = []
    for t_c, k_c in zip(text, key):
        t = alphabet_dict[t_c] + 1
        k = alphabet_dict[k_c] + 1
        if decode:
            tk = t - k + len(alphabet_list)
        else :
            tk = t + k
        mod = tk % len(alphabet_list)
        if mod == 0:
            mod = len(alphabet_list)
        result.append(alphabet_list[mod - 1])
    return ''.join(result)