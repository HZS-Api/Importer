#!/bin/bash

if [[ "$(docker images -q lambda 2> /dev/null)" == "" ]]; then
  echo "Building Docker image ..."
  docker build -t lambda .
fi

docker run \
  -v $PWD:/var/task/ \
  lambda \
  flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics --exclude .git,__pycache__,.pytest_cache,.idea,package,venv,local
