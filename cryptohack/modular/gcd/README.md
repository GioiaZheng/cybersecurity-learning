# GCD – Greatest Common Divisor

**Category:** Mathematics  
**Points:** 15  

This challenge introduces one of the most fundamental algorithms in number theory:
the **Greatest Common Divisor (GCD)** and the **Euclidean Algorithm**.

---

##  What I Learned

- Definition of GCD: the largest integer that divides both numbers  
- How to compute GCD efficiently using **Euclid’s Algorithm**  
- Why replacing `(a, b)` with `(b, a % b)` preserves the GCD  
- That the algorithm always terminates because the remainder strictly decreases  
- That prime numbers are automatically coprime with any smaller number  
- Why GCD is essential in:
  - RSA (checking if two numbers are coprime)  
  - Modular inverses (`gcd(a, m) = 1` is required)  
  - Extended Euclidean Algorithm  

---

##  Method

The Euclidean Algorithm is based on this rule:

> `gcd(a, b) = gcd(b, a mod b)`

Algorithm idea:

1. While `b != 0`:
   - Replace `(a, b)` with `(b, a % b)`
2. When `b` becomes `0`, the value of `a` is the GCD  
3. The **last non-zero remainder** is the answer.

For this challenge we are given:

- `a = 66528`  
- `b = 52920`  

Applying the algorithm step by step:

- `66528 = 52920 × 1 + 13608` → `gcd(66528, 52920) = gcd(52920, 13608)`  
- `52920 = 13608 × 3 + 12096` → `gcd(52920, 13608) = gcd(13608, 12096)`  
- `13608 = 12096 × 1 + 1512` → `gcd(13608, 12096) = gcd(12096, 1512)`  
- `12096 = 1512 × 8 + 0` → stop here  

So the last non-zero remainder is `1512`, hence:

> **`gcd(66528, 52920) = 1512`**

---

##  Relevance to Cryptography

GCD is used to:

- Check if two numbers are **coprime** (very important in RSA)  
- Compute **modular inverses** via the extended Euclidean algorithm  
- Support CRT (Chinese Remainder Theorem) and many number-theoretic constructions  

This problem is a warm-up for extended GCD, modular inverses, RSA, and CRT challenges.

---

##  Status

Challenge solved on CryptoHack.  
The answer is computed programmatically in `solve.py`.
