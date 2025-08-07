#!/usr/bin/env python3
"""
* collects/aggregates new DEC or TASK markdown files
* appends them into records/decision_log.yaml  and task_log.yaml
"""
import yaml, hashlib, datetime, pathlib, re

ROOT = pathlib.Path(__file__).resolve().parent.parent
DEC_DIR = ROOT / "docs/adr"
TASK_DIR = ROOT / "docs/tasks"
REC_DIR = ROOT / "records"
REC_DIR.mkdir(exist_ok=True)

def md_to_dict(md_path: pathlib.Path, kind:str):
    """front-matter を辞書化し、ハッシュ ID も付与"""
    text = md_path.read_text(encoding="utf-8")
    front = re.split(r"^---$", text, flags=re.MULTILINE)[1]
    meta = yaml.safe_load(front)
    meta["file"] = str(md_path.relative_to(ROOT))
    meta["digest"] = hashlib.sha1(text.encode()).hexdigest()[:8]
    meta["collected_at"] = datetime.datetime.now().isoformat(timespec="seconds")
    if kind=="decision": meta.setdefault("related_tasks", [])
    if kind=="task":     meta.setdefault("related_decision", None)
    return meta

def load_yaml(p): return yaml.safe_load(p.read_text()) if p.exists() else {"decisions":[],"tasks":[]}

# 1) 既存ログ読み込み
dec_log = load_yaml(REC_DIR/"decision_log.yaml")
task_log= load_yaml(REC_DIR/"task_log.yaml")

# 2) 新規 ADR / TASK を収集
for md in DEC_DIR.glob("*.md"):
    if not any(d["file"]==str(md.relative_to(ROOT)) for d in dec_log["decisions"]):
        dec_log["decisions"].append(md_to_dict(md,"decision"))
for md in TASK_DIR.glob("*.md"):
    if not any(t["file"]==str(md.relative_to(ROOT)) for t in task_log["tasks"]):
        task_log["tasks"].append(md_to_dict(md,"task"))

# 3) ソート & 上書き保存
dec_log["decisions"].sort(key=lambda d:d["date"])
task_log["tasks"].sort(key=lambda t:t["date"])
(REC_DIR/"decision_log.yaml").write_text(yaml.safe_dump(dec_log, allow_unicode=True, sort_keys=False))
(REC_DIR/"task_log.yaml").write_text(yaml.safe_dump(task_log , allow_unicode=True, sort_keys=False))
print("✅  Ledgers regenerated")
