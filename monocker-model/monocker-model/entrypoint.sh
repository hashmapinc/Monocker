#!/bin/bash

#start tf serving
tensorflow_model_server --port=9000 --model_config_file="/monocker-model/model_server_config.conf" &

#start registrant
python /monocker-model/registrant.py