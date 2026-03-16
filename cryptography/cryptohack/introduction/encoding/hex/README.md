# Hex

**Category:** Encoding  
**Points:** 5  

This challenge introduces hexadecimal encoding, which is commonly used to represent raw bytes in a human-readable form.

The given hex string represents a flag encoded as bytes. To decode it, convert the hex string into bytes and then into ASCII characters.

---

##  What I Learned
- `bytes.fromhex()` converts hex → bytes  
- `.hex()` converts bytes → hex  
- Hex is widely used in cryptography (keys, ciphertext, signatures, hashes)  
- Every 2 hex characters = 1 byte = 8 bits  
- Hex encoding is essential for understanding encrypted data

---

##  Method (Python)
```python
bytes.fromhex(hex_string).decode()
````

---

## ✔️ Status

Challenge completed successfully.
Flag is **not included** in this repository to comply with CryptoHack rules.
