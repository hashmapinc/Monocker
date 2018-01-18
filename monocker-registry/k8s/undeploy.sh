#!/bin/bash

# undeploy service
kubectl delete service monocker-registry-service

# optional - undeploy dev service for local machine http access to registry
kubectl delete service monocker-registry-service-dev

# undeploy deployment (haha)
kubectl delete deployment monocker-registry.deployment

# undeploy persistent volume claim
kubectl delete pvc monocker-registry.pvc

# undeploy persistent volume
kubectl delete pv monocker-registry.pv
