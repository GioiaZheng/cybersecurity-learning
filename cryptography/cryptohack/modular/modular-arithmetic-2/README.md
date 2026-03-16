# Modular Arithmetic 2

**Category:** Introduction  
**Points:** 20  

This challenge builds on the idea of modular arithmetic and introduces the
special case where the modulus is a **prime number**. When the modulus `p` is
prime, the integers modulo `p` form a structure called a **finite field**, often
written as **Fₚ**.

In a finite field Fₚ:

- Every non-zero element has a multiplicative inverse  
- Arithmetic behaves in a very structured and predictable way  
- Fermat’s Little Theorem holds:  
  `a^(p−1) ≡ 1 (mod p)` for all non-zero `a`

---

## What I Learned

- The difference between a ring (mod n) and a field (mod prime p)  
- Why integers modulo a prime form a field Fₚ  
- Identity elements for addition (`0`) and multiplication (`1`)  
- How modular exponentiation works  
- How Fermat’s Little Theorem simplifies large exponent calculations  
- How Python handles very large integers with ease  

---

## Method

1. Work in the finite field F₁₇ by setting `p = 17`.  
2. Compute modular powers such as `3^17 mod 17`, `5^17 mod 17`, and `7^16 mod 17`.  
   These expressions are simplified using the fact that `a^(p−1) ≡ 1 (mod p)`  
   whenever `a` is not divisible by `p`.

3. Repeat the same idea for the large prime `p = 65537`.  
   The exponent `65536` is exactly `p−1`, making Fermat’s Little Theorem apply
   immediately.

4. Python is used to perform the computations, but the core insight comes from
   number theory, not brute force.

---

## Status

Challenge solved on CryptoHack.  
All numerical results and flags are intentionally omitted, following CryptoHack rules.
