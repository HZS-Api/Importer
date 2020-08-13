#!/bin/bash

if [[ "$(docker images -q lambda 2> /dev/null)" == "" ]]; then
  echo "Building Docker image ..."
  docker build -t lambda .
fi

docker run \
  -v $PWD/src:/var/task/ \
  lambda \
  import.lambda_handler \
  '{"url": "https://www.hzspa.cz/vyjezdy/rss-aktualni-vyjezdy.php"}'
