#!/bin/bash

docker run --rm -it \
    -p 5000:5000 \
    -v ~/projects/Monocker/monocker-registry/monocker_registry:/mnt/monocker_registry \
    ${USER}/monocker-registry 