#!/bin/sh

# Delete all .DS_Store files
git filter-branch --force --index-filter '
git rm --cached -f --ignore-unmatch *.DS_Store
' --prune-empty --tag-name-filter cat -- --all

# Delete all __pycache__ folders
git filter-branch --force --index-filter '
git rm -r --cached -f --ignore-unmatch **.pyc
' --prune-empty --tag-name-filter cat -- --all