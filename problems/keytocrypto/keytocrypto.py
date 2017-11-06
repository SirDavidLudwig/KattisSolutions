import sys

cipher = sys.stdin.readline().strip()
key = sys.stdin.readline().strip()
message = ""

for i in range(len(cipher)):
	message += chr((ord(cipher[i])-65-(ord(key[i] if i < len(key) else message[i-len(key)])-65))%26+65)
print(message)
