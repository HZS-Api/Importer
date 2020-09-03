#!/bin/bash

if [[ "$(docker images -q lambda 2> /dev/null)" == "" ]]; then
  echo "Building Docker image ..."
  docker build -t lambda .
fi

docker run \
  -v $PWD:/var/task/ \
  lambda \
  /var/rapid/init --bootstrap /var/runtime/bootstrap --enable-msg-logs src/import.lambda_handler \
  '{"url": "https://www.hzspa.cz/vyjezdy/rss-aktualni-vyjezdy.php"}'
