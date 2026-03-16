# Modular Arithmetic 1

**Category:** Introduction  
**Points:** 20  

This challenge introduces the basic idea of **modular arithmetic**, the same
mathematics used when we compute time on a 12-hour clock.  
We are given two congruences:

- `11 ≡ x (mod 6)`  
- `8146798528947 ≡ y (mod 17)`

The task is simply to compute both remainders and then take the **smaller**
between the two integers `(x, y)`.

---

## What I Learned

- How modular arithmetic describes values **modulo** a positive integer  
- What it means for two numbers to be **congruent modulo m**  
- How to compute the remainder of an integer using Python’s `%` operator  
- Why congruences behave like “clock arithmetic”  
- How to translate a mathematical congruence into code  

---

## Method

1. Interpret the expressions  
   - `x = 11 mod 6`  
   - `y = 8146798528947 mod 17`

2. Use Python's `%` operator to compute each remainder.

3. Compare the two results and keep the smaller integer.  
   (The challenge does **not** require storing or printing any flag.)

No flag appears in this exercise; the goal is simply to understand congruences
and remainder computations.

---

## Status

Challenge solved on CryptoHack.  
This repository does **not** include the final numeric outputs, respecting
CryptoHack rules.
