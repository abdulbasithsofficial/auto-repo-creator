# AutoRepo-Agent
Benefit: Creates a new GitHub repo project folder from a name, description and template, with README, LICENSE and .gitignore already in place — without overwriting anything that already exists.

## What it does
In dry-run/local mode it creates a local project folder for the new repo, writes a README, MIT LICENSE and a template .gitignore, and prints the steps to push it to GitHub. It refuses to overwrite an existing folder.

## Quick start
```bash
python3 agent.py --name my-new-tool --description "A small tool that does X" --template python --dry-run
python3 agent.py --name my-new-tool --description "A small tool that does X" --template python
```

## How to run
- `--dry-run` prints what would be created and creates nothing.
- Without `--dry-run` it creates `./output/<name>/` locally. Pushing to GitHub still needs your own GitHub account and credentials, which this tool never asks for in chat.
- Templates: `python`, `node`, `empty`.
