# Notes — Greatest Common Divisor (GCD)

This challenge teaches the **Euclidean Algorithm**, one of the oldest and most elegant algorithms in mathematics.  
It dates back to Euclid (~300 BC) and is still essential in modern cryptography.

---

## 1. What is GCD?

For integers `a` and `b`, the **Greatest Common Divisor** is the largest integer that divides both.

Example:

- Divisors of 12 → {1, 2, 3, 4, 6, 12}  
- Divisors of 8 → {1, 2, 4, 8}  
→ **gcd(12, 8) = 4**

Two numbers with `gcd(a, b) = 1` are called **coprime**.

---

## 2. Euclidean Algorithm — Why It Works

Key observation:

> Replacing `(a, b)` with `(b, a % b)` does not change the GCD.

Reason:

- If a number divides both `a` and `b`
- It must also divide any linear combination `a - k·b`
- And therefore divides `a % b`

This allows the algorithm to shrink numbers quickly.

The rule is:

> **gcd(a, b) = gcd(b, a % b)**

---

## 3. Step-by-Step Computation for This Challenge

We need to compute:

```

gcd(66528, 52920)

```

### Step 1
```

66528 = 52920 × 1 + 13608

```
→ Next: `gcd(52920, 13608)`

### Step 2
```

52920 = 13608 × 3 + 12096

```
→ Next: `gcd(13608, 12096)`

### Step 3
```

13608 = 12096 × 1 + 1512

```
→ Next: `gcd(12096, 1512)`

### Step 4
```

12096 = 1512 × 8 + 0

```

Remainder becomes `0`, so the last non-zero remainder is the GCD:

> **gcd = 1512**

---

## 4. Why GCD Matters in Cryptography

GCD appears everywhere in crypto:

###  Checking RSA key validity  
`e` must satisfy:

- `gcd(e, φ(n)) = 1`

Otherwise no private key exists.

###  Modular inverses  
`a⁻¹ mod m` exists **only if**:

> **gcd(a, m) = 1**

Used in:

- RSA encryption/decryption  
- Chinese Remainder Theorem  
- Diffie–Hellman  
- Lattice reductions  

###  Extended Euclidean Algorithm  
It solves:

```

a·x + b·y = gcd(a, b)

```

This is critical for:

- computing modular inverses  
- deriving RSA private exponent `d`  
- CRT recombination  

---

## 5. Summary

- Euclid’s Algorithm is simple yet extremely powerful  
- It runs in logarithmic time  
- It is used in nearly every number-theoretic cryptosystem  
- GCD is the foundation for modular inverses, CRT, and RSA  

This challenge ensures your mathematical foundations are solid before moving deeper into cryptography.
