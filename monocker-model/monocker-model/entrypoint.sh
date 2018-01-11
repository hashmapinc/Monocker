#!/bin/bash

#start tf serving
tensorflow_model_server --port=9000 --model_name=mnist --model_base_path=/tmp/mnist_model &

#start registrant
python /monocker-model/registrant.py