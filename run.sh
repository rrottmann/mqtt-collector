#!/bin/bash

[ -d "$(pwd)/data" ] || mkdir -p "$(pwd)/data"

docker build -t rottmrei/mqtt-wifi-collector .
docker run -d --rm -v $(pwd)/data:/data -it rottmrei/mqtt-wifi-collector