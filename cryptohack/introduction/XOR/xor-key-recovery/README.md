# XOR Key Recovery

**Category:** XOR  
**Points:** 30  

This challenge uses everything from the introductory XOR section:
hex decoding, XOR properties, known plaintext, and repeating-key XOR.

We're given a ciphertext encrypted with an unknown XOR key.  
By using the known flag prefix (`crypto{`), we can recover the key and decrypt the message.

---

##  What I Learned

- How to decode hex into bytes with `unhexlify`
- XOR’s reversibility (`C ^ K = P` → `C ^ P = K`)
- Known-plaintext attacks
- Detecting repeating-key XOR (“Vigenère-style XOR”)
- How to apply XOR byte-by-byte using Python
- Recognizing patterns to reconstruct the full key

---

##  Method Overview

1. Convert the provided ciphertext from hex to raw bytes  
2. Use the known plaintext `"crypto{"` to recover part of the key  
3. Notice the recovered bytes form readable ASCII → guess full key  
4. Decrypt using repeating-key XOR  
5. Recover the flag (not included)

---

##  Solve Script

See `solve.py` for the full annotated solution.

---

##  Status

Challenge solved on CryptoHack.  
The flag is **not included** to respect platform rules.
