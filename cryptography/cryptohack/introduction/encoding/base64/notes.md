# Notes — Base64

Base64 is an encoding scheme that converts binary data into a 64-character alphabet:
A–Z, a–z, 0–9, +, /

It works by processing data in blocks of 3 bytes (24 bits):

- 3 bytes → split into 4 groups of 6 bits  
- Each 6-bit value maps to one Base64 character  
- Adds `=` padding if needed  

---

##  Key Python Functions

### Hex → Bytes
```python
bytes.fromhex(hex_string)
````

### Bytes → Base64

```python
base64.b64encode(data)
```

### Bytes → ASCII String

```python
.decode()
```

---

##  Why Base64 matters in cryptography

* Used in PEM certificates (`-----BEGIN CERTIFICATE-----`)
* Used in JWT tokens
* Used in HTTP authentication headers
* Output format of many cryptographic functions
* Helps represent binary ciphertext in readable form

---

##  Completion
Decoded successfully.
Flag is not stored here to respect CryptoHack guidelines.
