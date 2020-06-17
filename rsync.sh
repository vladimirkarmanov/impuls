#!/bin/bash
rsync -avzP --exclude='.vscode' --exclude='.git' --exclude='.idea' --exclude='venv' --exclude='.gitignore' \
          --exclude='node_modules' --exclude='package-lock.json' --exclude='package.json' \
          --exclude='.pytest_cache' --exclude='requirements-dev.txt' --exclude='db.sqlite3' \
          --exclude='__pycache__' --exclude='rsync.sh' --exclude='gulpfile.js' \
          -e ssh /home/vladimir/projects/impuls root@ip:/home/projects