# Notes — Hex

Hexadecimal (base-16) allows encoding of binary data in a compact text format.  
One byte is represented by two hex characters:

- Example: `0x63` → ASCII `'c'`

---

##  Key Concepts
###  Hex → Bytes
```python
bytes.fromhex("636f6f6c")
````

###  Bytes → Hex

```python
b"cool".hex()
```

###  Bytes → ASCII

```python
.decode()
```

---

##  Why Hex Is Important in Cryptography

* Ciphertexts are raw bytes → often shown as hex
* Keys are often represented in hex
* Hash values (SHA-256, MD5, etc.) output hex
* Signatures & RSA moduli use hex frequently

---

##  Completion

Decoded successfully.
Flag hidden for security.
