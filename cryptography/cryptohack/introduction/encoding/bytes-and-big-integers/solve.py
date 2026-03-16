# CryptoHack Challenge: Bytes and Big Integers
# Convert a big integer back into a byte message.

from Crypto.Util.number import long_to_bytes

n = 11515195063862318899931685488813747395775516287289682636499965282714637259206269

msg = long_to_bytes(n)

print("Decoded message (inspect locally to see the flag).")
# If you want to see the actual message, uncomment one of the lines below:
# print(msg)              # raw bytes
# print(msg.decode())     # UTF-8 string
