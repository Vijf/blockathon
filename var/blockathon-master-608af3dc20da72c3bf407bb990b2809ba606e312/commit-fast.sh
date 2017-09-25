#!/usr/bin/env bash

git add .

read -p "Commit message: " commitmsg

if [[ -z "$commitmsg" ]]; then
    git commit -m "Snelle commit"
else
    git commit -m "$commitmsg"
fi

git push