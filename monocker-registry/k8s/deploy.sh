#!/bin/bash

# deploy service
kubectl create -f ./monocker-registry-Service.yaml

# deploy persistent volume
kubectl create -f ./monocker-registry-PV.yaml

# deploy deployment (haha)
kubectl create -f ./monocker-registry-Deployment.yaml

# optional - deploy dev service for local machine http access to registry
kubectl create -f ./monocker-registry-Service-dev.yaml