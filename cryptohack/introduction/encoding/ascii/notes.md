# Notes — ASCII

ASCII is a 7-bit encoding where each character is represented by an integer from 0 to 127.

---

##  Key Concepts
- `chr(n)` → converts integer `n` to a character  
- `ord(c)` → converts character `c` to its integer ASCII code  
- ASCII is widely used in cryptography when representing plaintext, ciphertext, or keys as numbers

---

##  Example
For the list:

````

[99, 114, 121, ...]

````

We decode using:

```python
"".join(chr(o) for o in ords)
````

---

##  Security Note

Actual flag is intentionally not stored in this repository.


