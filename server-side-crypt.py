"""This file will decode the input from the API. The key exchange mechanism is the one proposed by Diffie-Hellman where
a public key is exchanged and this one decoded using their own private keys. Two line-equations are used to simulate this
Input X output Y"""

import random


# -------------VARIABLES------------#
M = 67 # gradient
N = 12 # y-intercept

mapping = {0: 'A', 1: 'w', 2: 'W', 3: 'S', 4: 'J', 5: 'U', 6: '3', 7: 'X', 8: 'm', 9: 'H', 10: 'Q', 11: 'x', 12: '8',
           13: '6', 14: '2', 15: 's', 16: 'k', 17: '9', 18: 'B', 19: 'C', 20: 'E', 21: 'L', 22: 'M', 23: '0', 24: '4',
           25: 'o', 26: 'h', 27: 'R', 28: 'j', 29: 'P', 30: 'K', 31: 'T', 32: 'd', 33: 'D', 34: 'f', 35: 'v', 36: '7',
           37: 't', 38: 'r', 39: 'e', 40: 'b', 41: 'z', 42: 'G', 43: 'i', 44: 'Y', 45: 'V', 46: 'F', 47: 'c', 48: 'I',
           49: 'l', 50: '5', 51: 'u', 52: 'g', 53: '1', 54: 'Z', 55: 'y', 56: 'a', 57: 'N', 58: 'q', 59: 'p', 60: 'n',
           61: 'O', 62: ' ', 63: '.'}


# -------------FUNCTIONS-------------#
def reverse_dict(dictionary):
    """Reverses dictionaries"""
    empty = {}
    for key, value in dictionary.items():
        empty[value] = key
    return empty


def input(API_gradient, API_intercept):
    """Convert X-coord into Y_coord. Returns Y-coord"""
    x_coord = random.randint(0,500)
    return API_gradient*x_coord+API_intercept

def output()