# Modular Arithmetic 2

This challenge introduces finite fields and demonstrates the power of
**Fermat’s Little Theorem**, which gives us an easy way to compute very large
modular exponentiations when the modulus is prime.

---

## 1. Finite Fields Fₚ

When the modulus `p` is prime, the set:

`{0, 1, 2, ..., p−1}`

forms a **field**, meaning:

- Addition has an inverse: for every `a`, there exists `b` such that  
  `a + b ≡ 0 (mod p)`
- Multiplication has an inverse for every non-zero `a`
- Identity elements:
  - Additive identity: `0`
  - Multiplicative identity: `1`

This is why working modulo a prime is so important in cryptography.

---

## 2. Fermat’s Little Theorem

If `p` is prime and `a` is not divisible by `p`, then:

```

a^(p−1) ≡ 1 (mod p)

```

An equivalent form is:

```

a^p ≡ a (mod p)

```

We will apply this repeatedly.

---

## 3. Calculations in F₁₇

### (1) 3^17 mod 17

Using the theorem:

- 3 is non-zero modulo 17  
- Therefore `3^16 ≡ 1 (mod 17)`

Rewrite:

`3^17 = 3^(16) * 3`

So:

`3^17 ≡ 1 * 3 ≡ 3 (mod 17)`

---

### (2) 5^17 mod 17

Same logic:

`5^16 ≡ 1 (mod 17)`

Thus:

`5^17 = 5^16 * 5 ≡ 1 * 5 ≡ 5 (mod 17)`

---

### (3) 7^16 mod 17

Direct application:

`7^16 ≡ 1 (mod 17)`

because the exponent is exactly `p−1`.

---

## 4. Large Prime: p = 65537

65537 is a well-known **Fermat prime** and is used in RSA.

We compute:

```

273246787654^65536 mod 65537

```

Since `65536 = p−1`, by Fermat’s theorem:

```

a^(p−1) ≡ 1 (mod p)

```

Therefore:

```

273246787654^65536 ≡ 1 (mod 65537)

```

This works regardless of how large the base number is, as long as it is not a
multiple of 65537.

---

## 5. Summary

- Finite fields Fₚ exist only when `p` is prime.  
- Every non-zero element has a multiplicative inverse.  
- Fermat’s Little Theorem simplifies exponentiation dramatically.  
- Large modular powers can be computed instantly by using number theory, not raw computation.  
- Python can compute these values, but the theorem is the real reason the results are simple.

Numerical outputs are omitted in this repository to comply with CryptoHack rules.
