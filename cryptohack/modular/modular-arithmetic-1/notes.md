# Modular Arithmetic 1

This challenge introduces the core idea of **modular arithmetic**, which is the
mathematical foundation for many cryptographic algorithms.  
It is the same principle used when calculating time on a clock.

---

## 1. Understanding Congruences

A congruence such as

`a ≡ b (mod m)`

means:

- When we divide `a` by `m`, the remainder is `b`;  
- Or equivalently, `m` divides `(a - b)`.

Example:

`11 ≡ 5 (mod 6)`

because `11 = 6 × 1 + 5`.

### Why this works like a clock

If you add 7 hours to 10 o’clock, you get 17 —  
but modulo 12, this becomes:

`17 ≡ 5 (mod 12)`

This mirrors how we compute time.

---

## 2. Using Python to Compute Remainders

Python provides the `%` operator, which computes:

```python
a % m
````

This returns the remainder when dividing `a` by `m`.

This directly translates the mathematical expression.

---

## 3. The Two Congruences in This Challenge

### (1) `11 ≡ x (mod 6)`

We compute:

```python
x = 11 % 6
```

This gives the remainder of 11 divided by 6.

### (2) `8146798528947 ≡ y (mod 17)`

Even though the integer is large, Python handles arbitrary-precision integers, so:

```python
y = 8146798528947 % 17
```

works exactly as expected.

---

## 4. Final Comparison

The challenge asks only for:

> the smaller of the two integers (x, y)

This means we compute:

```python
result = min(x, y)
```

No flag is involved in this problem; it is purely a warm-up exercise in modular arithmetic.

---

## 5. Summary

* Modular arithmetic expresses remainders after division
* Congruence notation `a ≡ b (mod m)` means “same remainder modulo m”
* Python’s `%` operator computes the remainder directly
* The challenge consists of evaluating two remainders and choosing the smaller
* Actual numeric outputs are intentionally omitted
