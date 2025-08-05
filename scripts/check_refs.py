#!/usr/bin/env python3
import yaml, pathlib, sys

dec_p = pathlib.Path('records/decision_log.yaml')
tsk_p = pathlib.Path('records/task_log.yaml')

dec = yaml.safe_load(dec_p.read_text())
tsk = yaml.safe_load(tsk_p.read_text())

tids = {t['id'] for t in tsk['tasks']}
dids = {d['id'] for d in dec['decisions']}
changed = False

# --- Decision to Task Link Cleanup ---
for d in dec['decisions']:
    if 'related_tasks' in d:
        # This part already handles lists correctly, no change needed.
        kept_tasks = [tid for tid in d.get('related_tasks', []) if tid in tids]
        if kept_tasks != d.get('related_tasks', []):
            changed = True
        if kept_tasks:
            d['related_tasks'] = kept_tasks
        else:
            d.pop('related_tasks', None)

# --- Task to Decision Link Cleanup (MODIFIED SECTION) ---
for t in tsk['tasks']:
    rids = t.get('related_decision')
    if rids:
        # Handle both single string and list of strings
        if isinstance(rids, str):
            # If a single, invalid ref is found, remove the key
            if rids not in dids:
                t.pop('related_decision', None)
                changed = True
        elif isinstance(rids, list):
            # If it's a list, keep only the valid decision IDs
            kept_decisions = [rid for rid in rids if rid in dids]
            if kept_decisions != rids:
                changed = True
            if kept_decisions:
                # If only one valid ref remains, store it as a string
                if len(kept_decisions) == 1:
                    t['related_decision'] = kept_decisions[0]
                else:
                    t['related_decision'] = kept_decisions
            else:
                t.pop('related_decision', None)

if changed:
    dec_p.write_text(yaml.safe_dump(dec, allow_unicode=True, sort_keys=False))
    tsk_p.write_text(yaml.safe_dump(tsk, allow_unicode=True, sort_keys=False))

# --- Final Hard Fail Check (MODIFIED SECTION) ---
miss_d2t = [(d['id'], tid) for d in dec['decisions'] for tid in d.get('related_tasks', []) if tid not in tids]

miss_t2d = []
for t in tsk['tasks']:
    rids = t.get('related_decision')
    if rids:
        # Normalize to a list to check all items
        if isinstance(rids, str):
            rids = [rids]
        for rid in rids:
            if rid not in dids:
                miss_t2d.append((t['id'], rid))

if miss_d2t or miss_t2d:
    if miss_d2t: print("Missing task references in decisions:", miss_d2t)
    if miss_t2d: print("Missing decision references in tasks:", miss_t2d)
    sys.exit(1)

print("All references are consistent.")