#!/bin/bash

docker run \
    --rm \
    -it \
    -p 5000:5000 \
    ${USER}/monocker-registry 