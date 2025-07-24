#!/usr/bin/env python3
import yaml, sys
from datetime import datetime, timezone
from dateutil import parser, relativedelta
REVIEW_CYCLE_DAYS = 90
GRACE_DAYS = 7
dec = yaml.safe_load(open('records/decision_log.yaml'))['decisions']
today = datetime.now(timezone.utc)
overdue = []
for d in dec:
    ts = parser.isoparse(d['timestamp'])
    due = ts + relativedelta.relativedelta(days=REVIEW_CYCLE_DAYS + GRACE_DAYS)
    if today > due and d.get('status') != 'reviewed':
        overdue.append((d['id'], str(due.date())))
if overdue:
    for i, dd in overdue: print(f"OVERDUE: {i} (due {dd})")
    sys.exit(1)
