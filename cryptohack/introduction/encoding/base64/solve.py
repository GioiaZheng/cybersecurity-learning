# CryptoHack Challenge: Base64
# Convert a hex string to bytes, then encode the result into Base64.

import base64

hex_string = "72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"

# Step 1: hex → bytes
data = bytes.fromhex(hex_string)

# Step 2: bytes → base64
b64_encoded = base64.b64encode(data)

print("Base64 result (flag hidden for GitHub safety):")
print("(Run locally to reveal the actual flag.)")
