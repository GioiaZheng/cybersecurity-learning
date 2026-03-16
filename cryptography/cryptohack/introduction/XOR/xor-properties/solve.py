from binascii import unhexlify

# Helper function: XOR two equal-length byte sequences
def xor(a, b):
    """
    XORs two byte strings by pairing each byte with zip()
    and returning a new bytes object.

    Example:
        xor(b"\x01\x02", b"\x03\x04") → b"\x02\x06"
    """
    return bytes([x ^ y for x, y in zip(a, b)])

# Step 1: Convert all hex strings to raw bytes

KEY1 = unhexlify("a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313")
KEY2_KEY1 = unhexlify("37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e")
KEY2_KEY3 = unhexlify("c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1")
FLAG_XOR  = unhexlify("04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf")

# Step 2: Recover KEY2 using XOR cancellation
# (KEY2 ^ KEY1) ^ KEY1 = KEY2

KEY2 = xor(KEY2_KEY1, KEY1)


# Step 3: Recover KEY3 similarly
# (KEY2 ^ KEY3) ^ KEY2 = KEY3

KEY3 = xor(KEY2_KEY3, KEY2)

# Step 4: Recover the FLAG
# FLAG = FLAG_XOR ^ KEY1 ^ KEY2 ^ KEY3
# Because each key appears twice originally and cancels out

tmp = xor(KEY1, KEY2)
tmp = xor(tmp, KEY3)
FLAG = xor(FLAG_XOR, tmp)

# Uncomment to print flag when running locally
# print(FLAG.decode())
