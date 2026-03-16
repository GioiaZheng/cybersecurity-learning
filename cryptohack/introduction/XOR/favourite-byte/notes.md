# Favourite byte — Notes

This challenge introduces **single-byte XOR**: a ciphertext has been produced by
XORing every byte of a plaintext with the same unknown byte key.

We are given a hex string:

```text
73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d
````

The goal is to recover the original message and the flag.

---

## 1. Decoding the Hex Ciphertext

The ciphertext is hex-encoded, so the first step is to turn it into raw bytes.

```python
from binascii import unhexlify

cipher_hex = "73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"
cipher = unhexlify(cipher_hex)
```

### What `unhexlify` does

* Takes a string of hexadecimal characters (0–9, a–f)
* Converts every two hex digits into one byte
* Returns a `bytes` object

Example:

```python
unhexlify("414243")  # b"ABC"
```

This conversion is necessary because XOR operates on numerical byte values,
not on hex strings.

---

## 2. XOR With a Single Byte

The encryption process in this challenge is:

```text
cipher[i] = plaintext[i] ^ key_byte
```

for each byte `i` of the message, where `key_byte` is a single integer in `[0, 255]`.

To reverse it, we use the fact that XOR is self-inverse:

```text
cipher[i] ^ key_byte = (plaintext[i] ^ key_byte) ^ key_byte = plaintext[i]
```

So if we try the correct key byte, we recover the original plaintext.

We implement a helper:

```python
def xor_with_byte(data, key):
    return bytes([b ^ key for b in data])
```

Explanation:

* Iterate over every byte `b` in `data`
* XOR it with the integer `key`
* Collect the results into a new `bytes` object

---

## 3. Brute-Forcing the Key

Because the key is only one byte, we can try all 256 possibilities.

```python
for k in range(256):
    candidate = xor_with_byte(cipher, k)
    try:
        text = candidate.decode()
        # Heuristic: keep only readable strings that look like CryptoHack flags
        if "crypto" in text:
            print(k, text)
    except UnicodeDecodeError:
        # Skip outputs that are not valid UTF-8
        continue
```

Why this works:

* Most keys will produce garbage bytes that cannot be decoded as UTF-8
* A few keys may decode, but the text will look random
* The correct key will yield a clean, readable English string starting with `crypto{...}`

This pattern (brute-forcing a small keyspace and scoring by readability) is a
standard technique in CTF cryptography.

---

## 4. Interpretation

From the loop, one key stands out as producing a valid-looking flag string.
That key is the correct single-byte XOR key, and the corresponding plaintext
contains the CryptoHack flag.

In this repository:

* The exact key value is known from solving the challenge,
  but **not stored** explicitly here.
* The printed flag is also omitted to keep the repository clean and compliant
  with CryptoHack rules.

---

## 5. Summary

* Hex → bytes via `binascii.unhexlify`
* Single-byte XOR implemented with list comprehension and `bytes([...])`
* Brute-force over all 256 possible keys
* Use UTF-8 decoding and `"crypto"` substring to filter candidates
* Recover the original message and flag successfully
Flag omitted intentionally.
