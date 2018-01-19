#!/bin/bash

# undeploy service
kubectl delete service monocker-api-service

# undeploy deployment (haha)
kubectl delete deployment monocker-api.deployment
