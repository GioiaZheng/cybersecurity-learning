# CryptoHack Challenge: Hex
# Decode a hex string into ASCII text.

hex_string = "63727970746f7b5961755f77696c6c5f616e645f6865785f737472696e67735f615f6c6f747d"

flag = bytes.fromhex(hex_string).decode()

print("Decoded flag (hidden on GitHub for safety):")
print("(Run locally to reveal the actual flag.)")
