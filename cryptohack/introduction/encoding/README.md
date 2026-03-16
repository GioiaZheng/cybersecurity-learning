# Encoding — CryptoHack Introduction

This folder contains all challenges related to **data encoding**, a foundational skill in
cryptography and CTF competitions.  
Encoding does not provide security, but it is the essential first step of every modern
cryptosystem — all ciphertexts, keys, signatures, and protocols require working with raw bytes.

Understanding encoding is the difference between *“I can write Python”* and *“I can analyze ciphertext”*.

---

##  What I Learned

### 1. ASCII (text → integers)
- `ord()` converts characters → integers.
- `chr()` converts integers → characters.
- Most classical ciphers and protocols operate on integer values, not letters.
- Essential for converting between human-readable text and low-level byte formats.

### 2. Hexadecimal (bytes → hex string)
- Hex is the standard format for representing arbitrary bytes.
- In Python:  
  ```python
  bytes.fromhex(hex_string)
  data.hex()
````

* Ciphers output bytes that may not be printable — hex makes them portable.

### 3. Base64 (binary → text-safe encoding)

* Base64 encodes binary data into ASCII-safe characters.
* Essential for:

  * Web APIs
  * JWT tokens
  * PEM certificates
  * Email / MIME
  * Many CTF challenges
* Python:

  ```python
  import base64
  base64.b64encode(data)
  base64.b64decode(data)
  ```

### 4. Bytes and Big Integers

* Convert long byte sequences into integers.
* Basic idea of how RSA and ECC encode plaintext.
* Learned to use:

  ```python
  from Crypto.Util.number import long_to_bytes, bytes_to_long
  ```
* Critical for future challenges like RSA attacks, modular arithmetic, padding analysis.

---

##  Why Encoding Is Important in CTFs and Cryptography

Encoding is the “language” of cryptography.
Without it, nothing else works.

###  Required for every crypto challenge

You must convert between:

* hex ↔ bytes
* bytes ↔ base64
* bytes ↔ integers
* integers ↔ ASCII

###  Required for cryptanalysis

Breaking RSA, AES, or ECC always begins with parsing:

* hex-encoded ciphertexts
* integer-encoded keys
* PEM/Base64 structures

###  Required for exploiting vulnerabilities

E.g.,

* Padding oracle → raw bytes
* JWT attacks → Base64 URL-safe
* XOR attacks → hex decoding
* Hash length extension → byte concatenation

If you cannot decode the input, you cannot attack the system.

---

##  Challenges Included

* ASCII
* Hex
* Base64
* Bytes and Big Integers
* Finding Flags
* Great Snakes

Flags are intentionally excluded.

---

##  Summary

This module taught me how **computers represent data** — the absolute foundation of all cryptography.
The skills here are essential for real-world CTFs, security engineering, and research.

Understanding encoding means understanding what ciphertext *really* is.
