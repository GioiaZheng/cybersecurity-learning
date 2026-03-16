# Bytes and Big Integers

**Category:** Encoding  
**Points:** 10  

This challenge shows how cryptosystems like RSA work with **integers**, while
our messages are usually **strings**. To apply mathematical operations, we
need a way to convert between bytes and big integers.

The common approach is:

1. Take the message as bytes  
2. Interpret the bytes as a big-endian integer  
3. Do math on the integer (e.g., RSA encryption)  
4. Convert the integer back into bytes and then into text  

---

##  What I Learned

- How messages can be transformed into big integers and back  
- In Python / PyCryptodome:

  - `bytes_to_long(b)` → bytes → integer  
  - `long_to_bytes(n)` → integer → bytes  

- This encoding is exactly what is used in RSA for plaintext and ciphertext.

---

##  Method (Python)

```python
from Crypto.Util.number import long_to_bytes

n = <given big integer>
msg = long_to_bytes(n)
msg.decode()
````

---

##  Status

Challenge solved successfully.
The actual flag is **not included** here to respect CryptoHack rules.
