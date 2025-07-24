#!/usr/bin/env python3
import yaml, glob, sys
targets = ["foundational_pillars", "evolutionary_roadmap"]
paths = glob.glob("constitution/**/*.yaml", recursive=True) + glob.glob("legislation/**/*.yaml", recursive=True)
hit = {k: [] for k in targets}
for p in paths:
    try:
        data = yaml.safe_load(open(p))
    except Exception:
        continue
    if isinstance(data, dict):
        for k in targets:
            if k in data:
                hit[k].append(p)
err = 0
for k, files in hit.items():
    if len(files) > 1:
        print(f"DUPLICATE {k}: {files}")
        err = 1
sys.exit(err)
