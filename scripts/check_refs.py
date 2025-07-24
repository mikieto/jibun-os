#!/usr/bin/env python3
import yaml, pathlib, sys
dec_p = pathlib.Path('records/decision_log.yaml')
tsk_p = pathlib.Path('records/task_log.yaml')
dec = yaml.safe_load(dec_p.read_text())
tsk = yaml.safe_load(tsk_p.read_text())
tids = {t['id'] for t in tsk['tasks']}
dids = {d['id'] for d in dec['decisions']}
changed = False
for d in dec['decisions']:
    if 'related_tasks' in d:
        kept = [tid for tid in d['related_tasks'] if tid in tids]
        if kept != d['related_tasks']:
            changed = True
        if kept: d['related_tasks'] = kept
        else: d.pop('related_tasks', None)
for t in tsk['tasks']:
    rid = t.get('related_decision')
    if rid and rid not in dids:
        t.pop('related_decision', None); changed = True
if changed:
    dec_p.write_text(yaml.safe_dump(dec, allow_unicode=True, sort_keys=False))
    tsk_p.write_text(yaml.safe_dump(tsk, allow_unicode=True, sort_keys=False))
# hard fail if still mismatch
miss_d2t = [(d['id'], tid) for d in dec['decisions'] for tid in d.get('related_tasks', []) if tid not in tids]
miss_t2d = [(t['id'], t.get('related_decision')) for t in tsk['tasks']
            if t.get('related_decision') and t['related_decision'] not in dids]
if miss_d2t or miss_t2d:
    print("Missing tasks:", miss_d2t)
    print("Missing decisions:", miss_t2d)
    sys.exit(1)
