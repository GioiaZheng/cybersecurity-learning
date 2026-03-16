# Notes — XOR Starter

##  What I Learned

* XOR works at the **bit level**
* Characters must be converted to **integers** with `ord()` before XOR
* XOR is **reversible**:

  > `x ^ k ^ k = x`
* Used everywhere in cryptography:

  * Stream ciphers
  * AES CTR mode
  * One-time pad
  * Masking
  * Many CTF challenges

These concepts build the foundation for later XOR challenges and real cryptographic attacks.

---

##  XOR Fundamentals

### Truth Table

| A | B | A⊕B |
| - | - | --- |
| 0 | 0 | 0   |
| 0 | 1 | 1   |
| 1 | 0 | 1   |
| 1 | 1 | 0   |

### Important Properties

* **Commutative**:  `a ^ b = b ^ a`
* **Associative**:  `(a ^ b) ^ c = a ^ (b ^ c)`
* **Self-canceling**: `a ^ a = 0`
* **Reversible**: `(x ^ k) ^ k = x`

This last property makes XOR a building block for encryption.

---

##  How XOR Works With Characters

Python cannot XOR characters directly — it must convert them to bytes/integers.

Example with `'l'`:

1. `'l'` → `ord('l') = 108`
2. `108 ^ 13 = new_number`
3. `chr(new_number)` → new character
4. Append to result string

This process is repeated for every character.

---

##  Final Code (Clean Version)

```python
s = "label"
result = "".join(chr(ord(c) ^ 13) for c in s)
print(result)
```

### Line-by-line Explanation

* `for c in s:`
  Iterates each char: `'l'`, `'a'`, `'b'`, `'e'`, `'l'`

* `ord(c)`
  Converts char → ASCII number

* `ord(c) ^ 13`
  XOR with integer 13

* `chr(...)`
  Convert back to a new character

* `"".join()`
  Combines all converted characters into a final string

---

##  Debug Notes

* Ensured using **Python 3.12** interpreter
* Verified output in terminal
* Printed intermediate values to understand ord/chr/XOR
* Full process now clear and repeatable for future challenges

---

##  Completion

XOR Starter completed successfully.
Flag intentionally omitted.
