# Monocker
[![Waffle.io - Columns and their card count](https://badge.waffle.io/8c69571d0e3c83af5edb071c43498612c4f9b1e3c202c89b3d8647adf33cd070.svg?columns=all)](https://waffle.io/hashmapinc/Monocker)

Monocker is a project for deploying machine learning and ANN models.

To install Monocker:

1. Clone this repo into your local environment
2. Follow the instructions below to install minikube if you don't have your own k8s cluster:
    https://kubernetes.io/docs/tasks/tools/install-minikube/
3. Follow the instructions below to install Helm if you don't have it already:
    https://docs.helm.sh/using_helm/#install-helm
4. From the repository root, run the following command:
```bash
helm install monocker
```

When monocker is finished loading in your k8s cluster, you will be able to access the UI at port ``` 30111 ``` on any node ip address in your cluster.
