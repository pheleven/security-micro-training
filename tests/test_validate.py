"""Exercise release-blocking packaging failures against disposable copies."""

import importlib.util
import json
from pathlib import Path
import shutil
import tempfile
import unittest

PROJECT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("validate", PROJECT / "scripts/validate.py")
validator = importlib.util.module_from_spec(spec)
spec.loader.exec_module(validator)


class PackagingTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name) / "skill"
        shutil.copytree(PROJECT, self.root, ignore=shutil.ignore_patterns(".git", "__pycache__"))

    def test_current_package(self):
        self.assertEqual(validator.validate(self.root), [])

    def test_missing_runtime_reference(self):
        (self.root / "references/hands-on.md").unlink()
        self.assertTrue(validator.validate(self.root))

    def test_broken_and_escaping_links(self):
        for link in ("missing.md", "../outside.md"):
            with self.subTest(link=link):
                page = self.root / "extra.md"
                page.write_text(f"[reference]({link})\n")
                self.assertTrue(validator.validate(self.root))

    def test_duplicate_case(self):
        path = self.root / "evals/cases.json"
        data = json.loads(path.read_text())
        data["cases"].append(data["cases"][0])
        path.write_text(json.dumps(data))
        self.assertTrue(validator.validate(self.root))

    def test_malformed_case_and_json(self):
        path = self.root / "evals/cases.json"
        for data in ('{', '{"schema_version":1,"cases":[null]}'):
            with self.subTest(data=data):
                path.write_text(data)
                self.assertTrue(validator.validate(self.root))

    def test_missing_frontmatter(self):
        (self.root / "SKILL.md").write_text("# Incomplete skill\n")
        self.assertTrue(validator.validate(self.root))


if __name__ == "__main__":
    unittest.main()
