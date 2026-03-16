# CryptoHack: Great Snakes
# This script decodes a list of integers using XOR with 0x32.

ords = [81, 64, 75, 66, 70, 93, 73, 72, 1, 92, 109, 2, 84, 109, 66, 75, 70]

def decode(nums, key=0x32):
    return "".join(chr(n ^ key) for n in nums)

if __name__ == "__main__":
    print("Decoded message (flag hidden):")
    print("(Run this locally to see the actual flag.)")
