#!/usr/bin/env bash

echo 'Deploying...'

# Frontend...
cp -r src/frontend/* /usr/share/nginx/html/

# Backend
cp -r src/* /usr/share/blockathon/src/
