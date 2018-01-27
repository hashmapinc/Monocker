#!/bin/bash

# deploy service
kubectl create -f ./monocker-api-dev-Service.yaml

# deploy deployment (haha)
kubectl create -f ./monocker-api-dev-Deployment.yaml
