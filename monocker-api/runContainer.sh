#!/bin/bash

docker run \
    --rm \
    -it \
    -p 80:80 \
    -v /Users/randypitcherii/projects/Monocker/monocker-api/monocker_api:/mnt/monocker_api \
    ${USER}/monocker-api  /bin/bash