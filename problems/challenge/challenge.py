import math


def reference_multiply(x: list, y:list):
    def convert_to_int(lst):
        result = 0
        for i in range(len(lst)):
            result += lst[i] * (2 ** i)
        return result
    result = convert_to_int(x) * convert_to_int(y)

    res_list = []
    while result > 0:
        res_list.append(result % 2)
        result = result // 2
    res_list.reverse()
    return res_list

def karatsuba(x, y):
    pass


def fft(x, y):
    pass
