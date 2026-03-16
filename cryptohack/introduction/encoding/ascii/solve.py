# CryptoHack Challenge: ASCII
# Convert a list of ASCII codes into characters.

ords = [99, 114, 121, 112, 116, 111, 123, 65, 83, 67, 73, 73, 95, 112, 114, 49, 110, 116, 52, 98, 108, 51, 125]

flag = "".join(chr(o) for o in ords)

print("Decoded flag (hidden for GitHub safety):")
print("(Run this script locally to see the actual flag.)")
