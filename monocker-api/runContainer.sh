#!/bin/bash

docker run \
    --rm \
    -it \
    -p 80:80 \
    ${USER}/monocker-api 