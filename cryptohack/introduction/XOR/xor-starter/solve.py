# XOR Starter – CryptoHack
# XOR each character in "label" with integer 13.

s = "label"
result = "".join(chr(ord(c) ^ 13) for c in s)

print("XOR result (run locally to see the decoded string):")
# print(result)  # Uncomment to see the full output
