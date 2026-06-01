# Security Checklist

Use this checklist before committing notes, scripts, or writeups.

## Do Not Commit

- Challenge flags or proof strings
- Passwords, API keys, tokens, cookies, or session identifiers
- Private keys, SSH configs, VPN profiles, or certificates
- Personal data, emails, account IDs, or student IDs
- Private IP addresses tied to real environments
- Screenshots containing secrets or identifiable account data
- Exploit output against systems that were not explicitly authorized labs

## Writeup Review

Before publishing a writeup:

1. Confirm the target is an authorized lab, CTF, course exercise, or local VM.
2. Replace secrets with placeholders such as `<redacted>` or `<flag omitted>`.
3. Keep commands reproducible, but remove values that identify private systems.
4. Add a defensive takeaway, not only the offensive path.
5. Separate observations from assumptions.
6. Record failed attempts when they explain the final method.

## Script Review

Before committing a script:

1. Add a short usage example.
2. Avoid hard-coded target hosts, credentials, or paths from private machines.
3. Use clear input arguments for target values.
4. Keep output safe to share.
5. Prefer deterministic examples that can run locally.

## Repository Hygiene

Recommended local checks:

```bash
git status --short
git diff --check
python scripts/security_review.py
python -m unittest discover -s tests
```

The GitHub Actions security review runs the same repository scanner and tests on
pushes and pull requests.

## Disclosure Boundary

This repository is for learning notes and authorized practice only. Do not use
it to publish instructions, credentials, or artifacts from unauthorized systems.
