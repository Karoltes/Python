import csv
import rsa


with open('keys.csv', 'a', newline='') as file:
    p = rsa.rand_prime()
    q = rsa.rand_prime()
    n = p * q
    phi = (p - 1) * (q - 1)
    e = rsa.calculate_e(phi)
    d = rsa.calculate_d(e, phi)
    keys = [[e, d, n]]
    csv_output = csv.writer(file)
    csv_output.writerows(keys)
