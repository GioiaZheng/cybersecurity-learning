#  CryptoHack-Solutions

This repository contains my solutions, notes, and Python scripts for the cryptography challenges on
[CryptoHack](https://cryptohack.org).
It documents my learning journey as I build a solid foundation in applied cryptography and CTF problem-solving.

---

##  About This Project

CryptoHack is an interactive platform for learning modern cryptography through hands-on challenges.
As I progress through the course modules and standalone challenges, I document:

- Clean, reproducible Python solutions (no flags included)
- Explanations and reasoning steps
- Insights into cryptographic concepts
- Debugging notes when issues arise
- Reusable helper functions for future challenges and CTFs

This repository serves as both a study log and a long-term cryptography reference.

---

##  Topics Covered

As I advance through CryptoHack, I explore core areas of applied cryptography:

### **Foundational Concepts**
- Data encoding (ASCII, hex, Base64)
- Byte–integer conversions
- XOR & bitwise logic
- Modular arithmetic

### **Applied Cryptography**
- Classical ciphers
- Stream cipher behavior through XOR
- CBC mode quirks
- Hashing concepts (later modules)

### **Number Theory**
- Modular inverses
- GCD & extended Euclidean algorithm
- Fermat, Euler φ, CRT
- Big integer manipulation

### **Public-Key Cryptography**
- RSA basics & vulnerabilities
- Padding oracle intuition
- Factoring and key recovery
- Understanding RSA implementation mistakes

### **Elliptic Curve Cryptography (ECC)**
- Group operations
- Scalar multiplication
- Curve structure
- Common ECC CTF techniques

---

##  Repository Structure

Active folders in this repo mirror the CryptoHack course order:

```
introduction/
├── encoding/             – Hex, Base64, ASCII, byte conversion warmups
└── XOR/                  – XOR logic and stream cipher intuition

modular/                  – Modular arithmetic and number theory
├── extended-gcd/
├── gcd/
├── general-mathematics/
├── mathematics-modular-math/  – Challenge set retaining the original site naming
├── modular-arithmetic-1/
└── modular-arithmetic-2/
```

Each challenge folder typically includes:

- `solve.py` – Clean solution script (flag removed)
- `README.md` – Explanation of the challenge
- `notes.md` – My thought process, mistakes, and learning

---

##  Goals

- Build a strong foundation in **applied cryptography**
- Learn offensive/CTF-style cryptographic reasoning
- Develop reusable tools for competitions and research
- Create a clear, organized portfolio of crypto knowledge
- Track learning progress through systematic documentation

---

##  Tech Stack

- **Python 3**
- **PyCryptodome**
- **pwntools (later challenges)**
- Optional: SageMath / sympy for math-heavy tasks

---

##  Disclaimer

This repository contains **only educational material**:
no challenge flags, no answer leaks, and no solutions meant to break real systems.
Everything is strictly for cryptography learning and CTF practice.
