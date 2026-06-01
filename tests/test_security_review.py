from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from scripts.security_review import scan_file, scan_repository


class SecurityReviewTests(unittest.TestCase):
    def test_common_flag_placeholders_are_allowed(self) -> None:
        with tempfile.TemporaryDirectory() as tmp_dir:
            path = Path(tmp_dir) / "notes.md"
            path.write_text(
                "\n".join(
                    [
                        "Use crypto{...} as a placeholder.",
                        "Example answer: crypto{something_here}",
                        "Published note: flag{flag omitted}",
                    ]
                ),
                encoding="utf-8",
            )

            self.assertEqual(scan_file(path), [])

    def test_realistic_ctf_flag_is_reported(self) -> None:
        with tempfile.TemporaryDirectory() as tmp_dir:
            path = Path(tmp_dir) / "writeup.md"
            flag = "crypto" + "{actual_secret_value}"
            path.write_text(f"Recovered value: {flag}\n", encoding="utf-8")

            findings = scan_file(path)

            self.assertEqual(len(findings), 1)
            self.assertEqual(findings[0].rule, "ctf-flag")
            self.assertEqual(findings[0].line_number, 1)

    def test_private_key_header_is_reported(self) -> None:
        with tempfile.TemporaryDirectory() as tmp_dir:
            path = Path(tmp_dir) / "key.txt"
            header = "-----BEGIN " + "OPENSSH PRIVATE KEY-----"
            path.write_text(f"{header}\n", encoding="utf-8")

            findings = scan_file(path)

            self.assertEqual(len(findings), 1)
            self.assertEqual(findings[0].rule, "private-key")

    def test_skips_git_directory(self) -> None:
        with tempfile.TemporaryDirectory() as tmp_dir:
            root = Path(tmp_dir)
            git_dir = root / ".git"
            git_dir.mkdir()
            token = "ghp_" + "exampletokenwithenoughcharacters123456"
            (git_dir / "config").write_text(f"token = {token}\n", encoding="utf-8")
            (root / "README.md").write_text("Clean learning notes.\n", encoding="utf-8")

            self.assertEqual(scan_repository(root), [])


if __name__ == "__main__":
    unittest.main()
