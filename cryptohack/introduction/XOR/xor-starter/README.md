# XOR Starter

**Category:** XOR  
**Points:** 10  

This challenge introduces the XOR operator, one of the most fundamental tools in
cryptography. XOR is used in stream ciphers, one-time pads, block cipher modes,
and many CTF-style attacks.

Given the string:

```

label

````

we must XOR each character with the integer `13`, convert the resulting integers
back to characters, and combine them into a new string.

---

##  Key Concepts

### XOR Truth Table

| A | B | A ⊕ B |
|---|---|--------|
| 0 | 0 | 0 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 0 |

Properties:

- `a ^ a = 0`
- `a ^ b = b ^ a`
- `(x ^ k) ^ k = x` (basis of stream encryption)

---

##  Python Approach

```python
result = "".join(chr(ord(c) ^ 13) for c in "label")
````

This computes the XOR of each character with `13` and builds the final string.

---

##  Status

The challenge was solved successfully.
Flag is not included here for CryptoHack integrity.
