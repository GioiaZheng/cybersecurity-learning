# XOR — CryptoHack Introduction

This folder contains all challenges related to the XOR operator — one of the most fundamental
operations in symmetric cryptography and CTF challenges.

XOR may look simple, but it is the core of:
- stream ciphers  
- OTP (One-Time Pad)  
- block cipher modes (CTR, OFB, CFB)  
- mask generation  
- bitwise operations in hash functions  
- many CTF crypto puzzles  

---

##  What I Learned

### 1. XOR at the bit level
- XOR truth table:
  - same bits → 0  
  - different bits → 1  
- Python uses `^` for XOR.

### 2. ASCII XOR
- Convert character → integer:
  ```python
  ord(c)
````

* XOR with a key:

  ```python
  ord(c) ^ key
  ```
* Convert back:

  ```python
  chr(...)
  ```

### 3. XOR with bytes

* Learned how to XOR byte strings safely:

  ```python
  bytes([a ^ b for a, b in zip(x, y)])
  ```
* How encryption and decryption are identical operations under XOR.

### 4. XOR Properties

These algebraic rules make XOR powerful:

* Commutative: `A ^ B = B ^ A`
* Associative: `(A ^ B) ^ C = A ^ (B ^ C)`
* Identity: `A ^ 0 = A`
* Self-inverse: `A ^ A = 0`
* Reversibility:

  ```
  cipher = plaintext ^ key
  plaintext = cipher ^ key
  ```

### 5. Recovering unknown keys

Using XOR chains:

* If `A ^ B = C`, then `A = B ^ C`.
* Used to recover KEY1, KEY2, KEY3 in “XOR Properties”.

### 6. Brute-forcing single-byte XOR

Learned how to try all `0–255` keys and check which XOR produces readable ASCII.

This technique is extremely important for:

* Breaking simple ciphertexts
* Solving classical CTF crypto puzzles
* Detecting XOR-encrypted shellcode or malware

---

##  Why XOR Is Important in CTFs and Cryptography

###  Stream ciphers are just XOR

OTP, RC4, ChaCha20 — all generate a keystream and XOR with plaintext.

###  AES-CTR = AES keystream + XOR

CTR mode turns AES into a stream cipher via XOR.

###  Malware obfuscation

Most malicious payloads use XOR encoding because it's fast and reversible.

###  Many CTFs hide data with XOR

Especially:

* single-byte XOR
* xor with repeating keys
* xor with derived keystreams
* xor chains similar to CryptoHack challenges

###  Reversibility makes cryptanalysis possible

XOR is invertible with the same key — no separate decrypt function.

---

##  Challenges Included

* XOR Starter
* XOR Properties
* Favourite Byte
* You either know, XOR you don’t

Flags are intentionally excluded.

---

##  Summary

This module gave me a complete understanding of XOR — from the bitwise definition to using
algebraic properties to extract keys and decrypt multi-layer XOR ciphertexts.

Mastering XOR is essential for:

* symmetric cryptography
* stream ciphers
* reverse engineering
* malware analysis
* CTF crypto puzzles

XOR is simple — but it is everywhere in cryptography.
