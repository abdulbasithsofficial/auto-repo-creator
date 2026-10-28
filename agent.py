#!/usr/bin/env python3
"""AutoRepo-Agent — draft-first local repo scaffolder. Refuses to overwrite."""
import argparse, os, sys
GITIGNORES = {"python": "__pycache__/\n*.pyc\n.env\n", "node": "node_modules/\n.env\n", "empty": ".env\n"}
def main():
    p = argparse.ArgumentParser(); p.add_argument("--name", required=True); p.add_argument("--description", default="")
    p.add_argument("--template", default="python", choices=["python", "node", "empty"]); p.add_argument("--dry-run", action="store_true")
    a = p.parse_args()
    out = os.path.join("output", a.name)
    if os.path.exists(out):
        print(f"REFUSED: {out} already exists. Choose a different name."); sys.exit(1)
    print(f"Would create: {out}/README.md, LICENSE, .gitignore (template={a.template})")
    if a.dry_run: print("Dry-run only: nothing created."); return
    os.makedirs(out)
    open(os.path.join(out, "README.md"), "w").write(f"# {a.name}\n\n{a.description}\n")
    open(os.path.join(out, "LICENSE"), "w").write("MIT License\n\nPermission is hereby granted, free of charge, to any person obtaining a copy of this software.\n")
    open(os.path.join(out, ".gitignore"), "w").write(GITIGNORES[a.template])
    print(f"Created {out}. Next: create the repo on GitHub, then push this folder.")
if __name__ == "__main__": main()
