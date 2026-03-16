# ASCII

**Category:** Encoding  
**Points:** 5  

This challenge introduces ASCII — a 7-bit character encoding standard (0–127).  
The task is to convert a list of integer codes into their corresponding ASCII characters.

---

##  What I Learned
- `chr()` converts an integer (0–127) into its ASCII character
- `ord()` converts a character back into its integer code
- How plaintext can be hidden as numeric arrays
- Basic encoding/decoding concepts used in cryptography

---

##  Method
Given a list of ASCII integer values:

```python
"".join(chr(o) for o in ords)
````

Decodes the flag.

---

##  Status

Challenge solved on CryptoHack.
The actual flag is **not included** to respect CryptoHack rules.

