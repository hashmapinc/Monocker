#!/bin/bash

docker run --rm -d -p 10010:10010 -p 81:81 ${USER}/monocker-registry 