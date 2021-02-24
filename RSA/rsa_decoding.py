import rsa

d, n = input("Enter private key: ").split()
d = int(d)
n = int(n)

with open('message.txt', 'r') as file:
    code = file.readline().split(sep=' ')
    code = code[:-1]
    code = [int(c) for c in code]

message = [rsa.decode_rsa(c, d, n) for c in code]
message = [chr(c) for c in message]

message = ''.join(message)

print(message)
