from binascii import unhexlify

# ---------------------------------------------------------
# Favourite byte – CryptoHack
# Single-byte XOR brute-force to recover the plaintext
# ---------------------------------------------------------

cipher_hex = "73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"
cipher = unhexlify(cipher_hex)


def xor_with_byte(data: bytes, key: int) -> bytes:
    """
    XOR every byte in 'data' with the same 1-byte key.

    Args:
        data: ciphertext as bytes
        key:  integer between 0 and 255

    Returns:
        New bytes object where each byte is data[i] ^ key
    """
    return bytes([b ^ key for b in data])


# Brute-force all possible 1-byte keys and print readable candidates.
# In practice, we filter by outputs that:
#  - decode as UTF-8
#  - contain the substring "crypto"
for k in range(256):
    candidate = xor_with_byte(cipher, k)
    try:
        text = candidate.decode()
    except UnicodeDecodeError:
        continue  # skip non-text outputs

    if "crypto" in text:
        print(f"key = {k} (0x{k:02x}) -> {text}")
        # Once found, you can use this key locally to extract the flag.
        # Do not commit the actual flag to the repository.
