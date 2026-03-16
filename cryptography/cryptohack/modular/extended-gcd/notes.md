# Extended Euclidean Algorithm — Notes

The **extended Euclidean algorithm (EEA)** is an extension of Euclid’s classical algorithm.
Instead of computing only the greatest common divisor:

```
gcd(a, b)
```

EEA computes **three values**:

```
(g, u, v)
```

such that:

```
a·u + b·v = g = gcd(a, b)
```

The integers **u** and **v** are known as **Bézout coefficients**.

---

## 1. Why the Euclidean Algorithm Works

The key identity:

```
gcd(a, b) = gcd(b, a mod b)
```

remains valid **even when tracking coefficients**.

If:

```
a = bq + r
```

then every number dividing both **a** and **b** must also divide **r**.

This gives the recursive structure of the Euclidean Algorithm:

* Replace `(a, b)` with `(b, r)`
* Track how each remainder is expressed using previous values
* When the remainder becomes 0, backtrack to express gcd as a linear combination of `(a, b)`

---

## 2. How the Extended Algorithm Works

The algorithm maintains **three sequences**:

```
r0 = a,   r1 = b
s0 = 1,   s1 = 0
t0 = 0,   t1 = 1
```

At each step:

```
r(i+1) = r(i) - q(i) * r(i-1)
s(i+1) = s(i) - q(i) * s(i-1)
t(i+1) = t(i) - q(i) * t(i-1)
```

When a remainder becomes **0**,
the Bézout coefficients are the **previous** `(s, t)`.

---

## 3. Applying EEA to This Challenge

Given:

* `p = 26513`
* `q = 32321`

Since both numbers are prime and distinct:

```
gcd(p, q) = 1
```

We want integers `u` and `v` such that:

```
p*u + q*v = 1
```

### Running the Extended Euclidean Algorithm

The computation yields:

```
u = -8404
v = 6893
```

Check:

```
26513 * (-8404) + 32321 * 6893 = 1
```

The answer (the smaller of the two numbers) is:

```
-8404
```

---

## 4. Why Extended GCD is Essential in Cryptography

###  Modular Inverses

A modular inverse `a⁻¹ mod m` exists **only if**:

```
gcd(a, m) = 1
```

EEA directly gives:

```
a⁻¹ ≡ u (mod m)
```

Used in:

* RSA decryption: `d ≡ e⁻¹ mod φ(n)`
* Diffie–Hellman key exchange
* Elliptic curve operations
* CRT calculations

---

###  Solving Linear Congruences

To solve:

```
a*x ≡ b (mod m)
```

EEA provides the exact solution.

---

###  RSA Key Recovery

To compute RSA private exponent:

```
d = e⁻¹ mod φ(n)
```

You must use the Extended Euclidean Algorithm.

---

## 5. Summary

* EEA computes `(g, u, v)` such that
  `a*u + b*v = gcd(a, b)`
* Bézout coefficients can be **negative**
* Essential for modular arithmetic, RSA, CRT, ECC
