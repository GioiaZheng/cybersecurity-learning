"""
Quadratic Residues — Modular Square Roots in F_p

This module demonstrates how to search for quadratic residues and compute
their modular square roots in a small finite field F_p.

All concrete numeric outputs and flags are intentionally omitted from
version control to comply with CryptoHack rules.
"""

from typing import List, Tuple, Dict


def modexp(a: int, e: int, m: int) -> int:
    """Fast modular exponentiation using Python's built-in pow()."""
    return pow(a, e, m)


def squares_mod_p(p: int) -> Dict[int, List[int]]:
    """
    Return a mapping x -> list of a such that a^2 ≡ x (mod p),
    for all a in {0, 1, ..., p-1}.
    """
    mapping: Dict[int, List[int]] = {}
    for a in range(p):
        x = (a * a) % p
        mapping.setdefault(x, []).append(a)
    return mapping


def find_quadratic_residue_and_roots(p: int, candidates: List[int]) -> Tuple[int, List[int]]:
    """
    Given a prime p and a list of candidate integers, find the first candidate
    that is a quadratic residue modulo p and return it together with its roots.

    Returns:
        (x, roots) where x is the quadratic residue from candidates,
        and roots is the list of a such that a^2 ≡ x (mod p).
    Raises:
        ValueError: if none of the candidates is a quadratic residue.
    """
    sq_map = squares_mod_p(p)

    for x in candidates:
        x_mod = x % p
        if x_mod in sq_map:
            return x, sq_map[x_mod]

    raise ValueError("No quadratic residue found among the given candidates.")


def main():
    p = 29
    ints = [14, 6, 11]

    x, roots = find_quadratic_residue_and_roots(p, ints)
    roots_sorted = sorted(roots)

    # Debug prints for local use only (remove or comment out if desired)
    print(f"Quadratic residue modulo {p}:", x)
    print(f"Roots (mod {p}):", roots_sorted)
    print(f"Smaller root:", roots_sorted[0])


if __name__ == "__main__":
    main()
