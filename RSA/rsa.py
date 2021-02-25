import secrets
import sympy
import math


def rand_prime():
    x = 4
    while not sympy.isprime(x):
        x = secrets.randbelow(2**16)
    return x


def calculate_e(w_phi):
    w_e = 2
    while math.gcd(w_phi, w_e) != 1:
        w_e += 1
    return w_e


def calculate_d(w_e, w_phi):
    w_d = 1
    while (w_d * w_e) % w_phi != 1:
        w_d += 1
    return w_d


def encode_rsa(x, w_e, w_n):
    return (x ** w_e) % w_n


def decode_rsa(x, w_d, w_n):
    n2 = 1
    temp = (x ** n2) % w_n
    value = 1
    if w_d & n2 == n2:
        value = value * temp
    n2 = n2 * 2
    while n2 < w_d:
        temp = (temp ** 2) % w_n
        if w_d & n2 == n2:
            value = value * temp
        n2 = n2 * 2
    return value % w_n



