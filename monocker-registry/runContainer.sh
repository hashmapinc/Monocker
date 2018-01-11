#!/bin/bash

docker run --rm -d -p 10010:10010 -p 81:81 -p 1521:1521 ${USER}/monocker-registry 