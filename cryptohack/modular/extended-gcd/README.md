# Extended GCD

**Category:** Mathematics  
**Points:** 20  

This challenge introduces the **extended Euclidean algorithm**, a fundamental tool
for number theory and modern public-key cryptography.

Unlike the normal Euclidean algorithm that computes only `gcd(a, b)`, the extended
version also finds integers `u` and `v` satisfying:

$$
a \cdot u + b \cdot v = \gcd(a, b)
$$

These integers `(u, v)` are called **Bézout coefficients**.

In the challenge we are given primes:

- `p = 26513`
- `q = 32321`

Because both are prime and different:

$$
\gcd(p, q) = 1
$$

The task is to compute integers `u` and `v` such that:

$$
p \cdot u + q \cdot v = 1
$$

The flag is the **smaller** of the two integers `u` and `v`
(the numeric value only — no `crypto{}` format).

---

## Why Extended GCD Matters

Extended GCD is used in almost every modern cryptographic algorithm:

- Computing **modular inverses**  
- Deriving **RSA private key** (`d ≡ e^{-1} mod φ(n)`)  
- Solving linear congruences  
- Chinese Remainder Theorem  
- Signature and key-exchange systems  

This challenge prepares you for:

- RSA arithmetic  
- CRT recombination  
- Modular inversion problems  
- Many real CTF crypto tasks  

---

## Files Included

- `solve.py` — Python script to compute `(g, u, v)`
- `notes.md` — Full explanation and step-by-step reasoning
- `README.md` — Overview of the challenge and its significance
