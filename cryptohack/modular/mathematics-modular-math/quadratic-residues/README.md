# Quadratic Residues

**Category:** Mathematics – Modular Math  
**Points:** 25  

## Overview

This challenge introduces **quadratic residues** in modular arithmetic. Given a
prime modulus `p` and a list of integers, the task is to determine which value
is a quadratic residue modulo `p` and then compute one of its square roots in
the field **Fₚ**.

A number `x` is called a quadratic residue modulo `p` if there exists an `a`
such that:

`a^2 ≡ x (mod p)`

Otherwise, `x` is a quadratic non-residue.

---

## What I Learned

- The definition of quadratic residues and non-residues in **Fₚ**  
- That not every element of **Fₚ** has a square root (roughly half do, half don’t)  
- How to search for modular square roots by brute force when `p` is small  
- Why each quadratic residue in a finite field has **two** square roots: `a` and `−a`  
- How to implement a simple quadratic-residue test and root finder in Python  

---

## Method

The solution proceeds as follows:

1. Work modulo `p = 29` and consider the list `ints = [14, 6, 11]`.  
2. For each candidate `x` in the list, scan all `a` in `{0, 1, ..., p−1}` and
   check whether `a^2 ≡ x (mod p)`.  
3. The value(s) for which such an `a` exists are quadratic residues; the others
   are non-residues.  
4. For the quadratic residue, record the two solutions `a` and `p − a`.  
5. The challenge asks to submit the **smaller** of these two roots.

Only the general strategy is described here. Concrete numerical results and the
final submitted value are intentionally omitted to comply with CryptoHack rules.

---

## Status

Challenge completed.  
No explicit outputs or flags are included in this repository.
