#!/bin/bash

if [[ "$(docker images -q lambda 2> /dev/null)" == "" ]]; then
  echo "Building Docker image ..."
  docker build -t lambda .
fi

docker run \
  -v $PWD:/var/task/ \
  lambda \
  pytest
