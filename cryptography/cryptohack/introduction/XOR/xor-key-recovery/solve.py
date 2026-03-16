from binascii import unhexlify

# ---------------------------------------------------------
# 1. Ciphertext provided by CryptoHack
# ---------------------------------------------------------
cipher_hex = "0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104"

# Convert the hex string into raw bytes
# XOR must be done on bytes, not hex characters
cipher = unhexlify(cipher_hex)


# ---------------------------------------------------------
# 2. Known plaintext: CryptoHack flags always start with:
#       crypto{
# We'll use this to recover the beginning of the key
# ---------------------------------------------------------
known_plain = b"crypto{"

# Find the part of the key used to encrypt the first 7 bytes
partial_key = bytes([c ^ p for c, p in zip(cipher[:7], known_plain)])

print("Partial key recovered:", partial_key)

# Inspecting partial_key reveals something human-readable, e.g. b"myXORke"
# So we guess the full key is the English phrase: "myXORkey"
key = b"myXORkey"

print("Using full key guess:", key)


# ---------------------------------------------------------
# 3. Decrypt the full ciphertext using repeating-key XOR
# The key repeats like: key[0], key[1], ..., key[7], key[0], key[1], ...
# ---------------------------------------------------------
plaintext = bytes(
    [c ^ key[i % len(key)] for i, c in enumerate(cipher)]
)

print("Decrypted plaintext:")
print(plaintext.decode())
