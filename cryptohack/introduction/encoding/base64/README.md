# Base64

**Category:** Encoding  
**Points:** 10  

This challenge demonstrates how Base64 encoding works.  
We are given a string encoded in hexadecimal, and the goal is to:

1. Decode the hex string into raw bytes  
2. Encode those bytes into Base64  

This mirrors real-world cryptography, where data is often represented in hex or Base64 for transport or storage.

---

##  What I Learned
- `bytes.fromhex()` converts a hex string into bytes  
- `base64.b64encode()` converts bytes into Base64  
- Base64 encodes every 3 bytes into 4 ASCII characters  
- Very common in protocols like TLS, JWT, PEM certificates, SSH keys, APIs, etc.

---

##  Method (Python)

```python
data = bytes.fromhex(hex_string)
base64.b64encode(data)
````

---

##  Status

Challenge successfully solved.

Flag is intentionally **not included** to comply with CryptoHack rules.
