# Favourite byte

**Category:** XOR  
**Points:** 20  

This challenge hides a message that has been XORed with a **single unknown byte**.  
The ciphertext is given as a hex string, and the task is to recover the plaintext
(and the flag) by discovering the correct byte key.

---

##  What I Learned

- How single-byte XOR encryption works  
- How to brute-force all possible 1-byte keys (0–255)  
- How to convert hex strings to bytes using `binascii.unhexlify`  
- How to XOR each byte of a ciphertext with the same key  
- How to filter candidate plaintexts by checking for readable ASCII / `"crypto"`  

---

##  Method

1. **Decode** the hex ciphertext into raw bytes  
2. For each key in the range `0..255`:
   - XOR every byte of the ciphertext with this key  
   - Attempt to decode the result as UTF-8 text  
   - Keep the candidates that look like English and contain `"crypto"`  
3. The correct key reveals a nicely readable flag in the format `crypto{...}`  

The key in this challenge turns out to be a single byte value.  
(Flag and exact key are intentionally not included here.)

---

##  Status

Challenge solved on CryptoHack.  
The actual flag is **not included** in this repository to respect CryptoHack rules.
