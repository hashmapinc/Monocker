#!/bin/bash

# undeploy service
kubectl delete service monocker-api-dev-service

# undeploy deployment (haha)
kubectl delete deployment monocker-api.dev.deployment
