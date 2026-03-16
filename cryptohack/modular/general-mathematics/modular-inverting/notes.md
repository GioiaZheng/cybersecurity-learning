# Modular Inverting — Notes

Multiplicative inverses are essential in modular arithmetic, especially within
finite fields **Fₚ**, where `p` is prime. This document explains the theory,
derivation, and reasoning behind the inverse computation used in this
challenge.

---

## 1. Background Theory

A multiplicative inverse of a number `g` modulo `p` is an integer `d` such that:

`g * d ≡ 1 (mod p)`

Key facts:

- A multiplicative inverse exists **iff** `g` is not divisible by `p`.  
- When `p` is prime, every non-zero element in **Fₚ** has a unique inverse.  
- Inverses are fundamental in CRT, RSA key generation, and elliptic-curve crypto.

---

## 2. Using Fermat’s Little Theorem

If `p` is prime and `g` is not divisible by `p`, then:

`g^(p−1) ≡ 1 (mod p)`

Rearranging gives:

`g^(p−2) ≡ g⁻¹ (mod p)`

This identity allows us to compute modular inverses through exponentiation.

For the challenge:

- `g = 3`
- `p = 13`

Thus the inverse is expressed symbolically as:

`3^(13−2) = 3^11 mod 13`

The numeric value is omitted, but the theoretical expression is retained.

---

## 3. Extended Euclidean Algorithm (Alternative Approach)

The inverse can also be found by solving:

`3d + 13k = 1`

The extended Euclidean algorithm finds integers `d` and `k` satisfying this
equation. The value of `d`, reduced modulo 13, is the multiplicative inverse.

This provides a more general method that works even when `p` is not prime.

---

## 4. Python Implementation Idea

Python implements fast modular exponentiation through:

```python
pow(base, exponent, modulus)
````

which internally uses exponentiation by squaring, optimized for very large
integers. When working with Fermat’s theorem, we simply compute:

```python
pow(g, p - 2, p)
```

to obtain the symbolic inverse.

---

## 5. Summary

* Multiplicative inverses exist in Fₚ for all non-zero elements.
* Fermat’s Little Theorem provides a simple formula: `g^(p−2)`
* Extended Euclidean Algorithm offers a general and efficient alternative.
* Python’s `pow()` directly supports modular inverses using Fermat’s identity.
* Final numeric values are intentionally omitted to comply with CryptoHack rules.
