#!/usr/bin/env python3
import sys, yaml, re, pathlib

gate_path = sys.argv[sys.argv.index("--gate") + 1]
gate = yaml.safe_load(open(gate_path))

dec_id_rx = re.compile(gate["id_pattern"]["decision"])
task_id_rx = re.compile(gate["id_pattern"]["task"])

date_rx = re.compile(r"\d{4}-\d{2}-\d{2}")
fail = False

def lint(path):
    text = path.read_text(encoding="utf-8")
    errors = []
    if "http" not in text:
        errors.append("missing citation url")
    if not date_rx.search(text):
        errors.append("missing YYYY-MM-DD date")
    if re.search(r"(latest|recent|yesterday)", text, re.IGNORECASE):
        errors.append("relative time expression")
    return errors

for f in pathlib.Path("docs/adr").rglob("**/*.md"):

    if "archive" in f.parts:
        continue

    err = lint(f)
    if err:
        print(f"❌ {f}: {', '.join(err)}")
        fail = True

print("✅ immune-lint passed" if not fail else "✖ lint failed")
sys.exit(1 if fail else 0)
