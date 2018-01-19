#!/bin/bash

# deploy service
kubectl create -f ./monocker-api-Service.yaml

# deploy deployment (haha)
kubectl create -f ./monocker-api-Deployment.yaml
