# Cybersecurity Learning Repository

> An engineering-oriented knowledge base for cybersecurity training, focused on **Linux foundations, practical pentesting, and cryptography challenge solving**.  
> This repository is designed to be **traceable, reproducible, and reusable** for long-term skill development.

---

## Table of Contents

- [1. Repository Purpose](#1-repository-purpose)
- [2. Top-Level Architecture](#2-top-level-architecture)
- [3. Module Breakdown](#3-module-breakdown)
  - [3.1 Linux Module](#31-linux-module)
  - [3.2 Pentesting Module](#32-pentesting-module)
  - [3.3 Cryptography Module](#33-cryptography-module)
- [4. Quick Start](#4-quick-start)
- [5. Recommended Learning Sequence](#5-recommended-learning-sequence)
- [6. Maintenance Principles](#6-maintenance-principles)
- [7. Templates and Safety](#7-templates-and-safety)

---

## 1. Repository Purpose

This repository is used to systematically document cybersecurity learning progress.

Core goals:

- **Structured knowledge capture**: Organize learning materials by domain for fast retrieval and iterative review.
- **Engineering-style organization**: Keep clear module boundaries (`Notes`, `Labs`, `Scripts`, `Challenges`).
- **Reusable assets**: Maintain scripts, command references, and solving workflows that can be reused in later labs/CTFs.

---

## 2. Top-Level Architecture

```text
.
|-- linux/
|   |-- essential/
|   `-- fundamentals/
|-- pentesting/
|   |-- tryhackme/
|   `-- hackthebox/
`-- cryptography/
    `-- cryptohack/
```

- Linux track entry: [`linux/`](linux/)
- Pentesting track entry: [`pentesting/`](pentesting/)
- Cryptography track entry: [`cryptography/`](cryptography/)

---

## 3. Module Breakdown

### 3.1 Linux Module

**Path**: [`linux/`](linux/)

#### (1) Essential Linux Training
- Module README: [`linux/essential/README.md`](linux/essential/README.md)
- Key directories:
  - Concept notes: [`linux/essential/Notes/`](linux/essential/Notes/)
  - Command references: [`linux/essential/Commands/`](linux/essential/Commands/)
  - Hands-on labs: [`linux/essential/Labs/`](linux/essential/Labs/)
  - Learning resources: [`linux/essential/Resources/`](linux/essential/Resources/)

This submodule builds command-line fundamentals, including filesystem operations, permissions, process handling, and networking tools.

#### (2) Linux Fundamentals
- Module README: [`linux/fundamentals/README.md`](linux/fundamentals/README.md)

This submodule is reserved for expanded Linux core concepts and foundational practice.

---

### 3.2 Pentesting Module

**Path**: [`pentesting/`](pentesting/)

#### (1) TryHackMe
- Module README: [`pentesting/tryhackme/README.md`](pentesting/tryhackme/README.md)
- Key directories:
  - Pathway tracking: [`pentesting/tryhackme/Pathways/`](pentesting/tryhackme/Pathways/)
  - Fundamentals: [`pentesting/tryhackme/Fundamentals/`](pentesting/tryhackme/Fundamentals/)
  - Room notes: [`pentesting/tryhackme/Rooms/`](pentesting/tryhackme/Rooms/)
  - PreSecurity path: [`pentesting/tryhackme/PreSecurity/`](pentesting/tryhackme/PreSecurity/)
  - Utility scripts: [`pentesting/tryhackme/Scripts/`](pentesting/tryhackme/Scripts/)

#### (2) Hack The Box
- Module README: [`pentesting/hackthebox/README.md`](pentesting/hackthebox/README.md)
- Key directories:
  - Academy studies: [`pentesting/hackthebox/Academy/`](pentesting/hackthebox/Academy/)
  - Machine practice: [`pentesting/hackthebox/Machines/`](pentesting/hackthebox/Machines/)
  - Challenge writeups: [`pentesting/hackthebox/Challenges/`](pentesting/hackthebox/Challenges/)
  - Practical scripts: [`pentesting/hackthebox/Scripts/`](pentesting/hackthebox/Scripts/)

This module follows a practical loop: **enumeration -> analysis -> exploitation -> review**.

---

### 3.3 Cryptography Module

**Path**: [`cryptography/`](cryptography/)

#### CryptoHack Study and Solutions
- Module README: [`cryptography/cryptohack/README.md`](cryptography/cryptohack/README.md)
- Current tracks:
  - Encoding introduction: [`cryptography/cryptohack/introduction/encoding/`](cryptography/cryptohack/introduction/encoding/)
  - XOR fundamentals: [`cryptography/cryptohack/introduction/XOR/`](cryptography/cryptohack/introduction/XOR/)
  - Modular arithmetic and number theory: [`cryptography/cryptohack/modular/`](cryptography/cryptohack/modular/)

Typical challenge folders include:
- `README.md`: challenge explanation and solution logic
- `notes.md`: thought process, pitfalls, and debugging notes
- `solve.py`: reproducible script

This module is intended to build mathematical intuition and CTF-grade cryptography problem-solving skills.

---

## 4. Quick Start

1. Clone and enter the repository:
   ```bash
   git clone <your-repo-url>
   cd cybersecurity-learning
   ```
2. Start with module entry READMEs:
   - [`linux/essential/README.md`](linux/essential/README.md)
   - [`pentesting/tryhackme/README.md`](pentesting/tryhackme/README.md)
   - [`pentesting/hackthebox/README.md`](pentesting/hackthebox/README.md)
   - [`cryptography/cryptohack/README.md`](cryptography/cryptohack/README.md)
3. Pick one track based on current learning stage and keep notes/scripts synchronized.

---

## 5. Recommended Learning Sequence

Suggested engineering-style progression:

1. **Linux fundamentals** (CLI, permissions, process control, networking basics)
2. **Security practice basics** (intro rooms/pathways on THM/HTB)
3. **Focused strengthening** (web security, privilege escalation, scripted enumeration)
4. **Cryptography training** (encoding/XOR/number theory toward public-key concepts)
5. **Review and standardization** (templates, tooling, and reusable methodology)

---

## 6. Maintenance Principles

- Keep directory structure stable for long-term navigation.
- Capture not only conclusions, but also process and failure cases.
- Prioritize script readability and reproducibility.
- Do not commit flags, credentials, or sensitive data.

---

## 7. Templates and Safety

- Standard writeup template: [`templates/writeup.md`](templates/writeup.md)
- Pre-commit safety checklist: [`SECURITY_CHECKLIST.md`](SECURITY_CHECKLIST.md)

Writeups should keep the practical reasoning reproducible while removing flags,
credentials, private infrastructure details, and account-specific data.
