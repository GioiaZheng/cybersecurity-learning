# Quadratic Residues — Notes

This challenge explores what it means for an integer to have a square root in
modular arithmetic, focusing on the finite field **Fₚ** with `p = 29`.

---

## 1. Definition: Quadratic Residue

Let `p` be an odd prime and consider the field Fₚ.

- An integer `x` (mod `p`) is a **quadratic residue** if there exists `a` such
  that:

  `a^2 ≡ x (mod p)`

- If no such `a` exists, then `x` is a **quadratic non-residue**.

Important facts:

- In Fₚ, roughly half of the non-zero elements are quadratic residues and the
  other half are non-residues.  
- If `a^2 ≡ x (mod p)` and `a ≠ 0`, then `(-a)^2 ≡ x (mod p)` as well, so
  every non-zero quadratic residue has **two** square roots: `a` and `p − a`.

---

## 2. Working Modulo 29

In this challenge we set `p = 29` and are given:

`ints = [14, 6, 11]`

We want to determine which of these is a quadratic residue modulo 29 and then
find its modular square root.

---

## 3. Brute Force Search for Square Roots

Since `p = 29` is small, we can simply try all possible values of `a` in
`{0, 1, ..., 28}` and check whether `a^2` matches any of the candidates modulo
29.

Conceptually, we:

1. Loop over `a` from 0 to 28.  
2. Compute `a^2 mod 29`.  
3. Compare the result with each candidate `x` in `[14, 6, 11]`.  
4. If a match is found, then `x` is a quadratic residue and `a` is one of its
   square roots.

From this process, one of the numbers in the list is discovered to be a
quadratic residue, and we obtain two solutions `a` and `29 − a`. The smaller of
these two is the value required by the CryptoHack challenge.

The actual numeric value is intentionally not recorded in this document.

---

## 4. Python Implementation Idea

We can codify the above brute-force method as:

```python
def squares_mod_p(p: int) -> dict[int, list[int]]:
    """Return a mapping x -> list of a such that a^2 ≡ x (mod p)."""
    mapping: dict[int, list[int]] = {}
    for a in range(p):
        x = (a * a) % p
        mapping.setdefault(x, []).append(a)
    return mapping
````

Given `ints = [14, 6, 11]`, we can:

1. Build `mapping = squares_mod_p(29)`
2. For each `x` in the list, check whether `x` is a key in `mapping`.
3. If it is, the associated list `mapping[x]` consists of the square roots of
   `x` modulo 29.

This directly reflects the mathematical reasoning above.

---

## 5. Summary

* Quadratic residues are numbers that admit modular square roots.
* In Fₚ, not every element is a quadratic residue; about half of the non-zero
  elements are.
* Each quadratic residue has two roots: `a` and `p − a`.
* For small primes, brute force is a perfectly valid way to detect residues and
  find roots.
* The challenge asks for the smaller root; the concrete value is produced by
  the script but omitted here to comply with CryptoHack rules.
