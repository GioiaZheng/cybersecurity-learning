# Modular Inverting

**Category:** General – Mathematics  
**Points:** 25  

## Overview

This challenge introduces the concept of **multiplicative inverses** in a finite
field **Fₚ**, where `p` is prime. The task is to determine the integer `d` such
that:

`g * d ≡ 1 (mod p)`

for a given non-zero element `g`. This problem appears frequently in number
theory and cryptography, particularly in RSA, Diffie–Hellman, and elliptic curve
operations.

---

## What I Learned

- The definition and properties of multiplicative inverses in **Fₚ**  
- Why inverses exist only when the modulus is prime  
- How **Fermat’s Little Theorem** can be used to compute inverses  
- The connection between inverses and modular exponentiation  
- The general idea behind solving `g * d ≡ 1 (mod p)`

---

## Method

The inverse of a number `g` modulo a prime `p` can be computed using:

1. **Fermat’s Little Theorem**, which states  
   `g^(p−2) ≡ g⁻¹ (mod p)`  
   when `g` is not divisible by `p`.

2. Alternatively, the **Extended Euclidean Algorithm** can be used to find `d`
   satisfying  
   `g*d + p*k = 1`.

3. Python’s `pow(g, p-2, p)` efficiently computes the exponentiation needed for
   the Fermat-based inverse.

All numerical outputs and final results are intentionally omitted from this file
in accordance with CryptoHack rules.

---

## Status

Challenge completed.  
No explicit outputs or flags are included in this repository.
