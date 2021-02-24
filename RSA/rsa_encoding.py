import rsa

message = input("Enter message to code in RSA: ")
e, n = input("Enter public key: ").split()
e = int(e)
n = int(n)

message = [ord(c) for c in message]
message = [rsa.encode_rsa(c, e, n) for c in message]

encoded_message = [str(c) for c in message]

with open('message.txt', 'w') as file:
    for s in encoded_message:
        file.write(s + " ")
