# Flask-Monitoring-Application
# GitOps with Argo CD

## Project Overview

The aim of this assignment is to understand the hands-on experience with GitOps practices, utilizing Argo CD for continuous deployment and Argo Rollouts for advanced deployment strategies within a Kubernetes environment. You will be responsible for setting up a GitOps pipeline that automates the deployment and management of a simple web application.

### Application Overview

Our application is a simple web application that displays system metrics such as CPU utilization and memory usage. It is built using Python Flask and utilizes the psutil library to collect system metrics. The application serves a single-page HTML template using Flask's render_template function.

### Prerequisites

Before getting started, ensure you have the following prerequisites installed:

- Docker.
- Git Bash.
- Minikube: To run a local Kubernetes cluster for testing purposes.

## Step-by-Step Guide

### Step 1: Install Minikube Locally

- Download and install Minikube locally using the following command:

```bash
Invoke-WebRequest -OutFile 'c:\minikube\minikube.exe' -Uri 'https://github.com/kubernetes/minikube/releases/latest/download/minikube-windows-amd64.exe' -UseBasicParsing
New-Item -Path 'c:\' -Name 'minikube' -ItemType Directory -Force
minikube start
```
## Verify that Minikube is running:
```bash
minikube status
```
## Step 2: Install Argo CD on Minikube
### Create a namespace for Argo CD:

```bash
kubectl create namespace argo
```
### Apply the Argo CD manifests:

```bash
kubectl apply -n argo -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml
```
### Check if Argo CD components are running:

```bash
kubectl get pods -n argo
```
### Retrieve the Argo CD admin password:

```bash
kubectl -n argo get secret argocd-initial-admin-secret -o jsonpath="{.data.password}" | base64 --decode 
```
### Note --> for powershell user use - 
```bash
kubectl -n argo get secret argocd-initial-admin-secret -o jsonpath="{.data.password}" 
```
and than go to your browser and search for base 64 decode and decode the encoded password you recieved and save the decoded password.  

### Forward the Argo CD server port to access the UI:
```bash
kubectl port-forward svc/argocd-server -n argo 8080:443
```
### Access the Argo CD UI by opening a web browser and navigating to https://localhost:8080 and logging in with username "admin" and the password retrieved earlier.
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
![Argo CD UI](https://github.com/Rohit3Pandey/Images/blob/main/Screenshot%20(103).png)

### Step 3: Deploy the Application with Argo CD
### Log in to the Argo CD UI.

### Create a new application with the following details:

#### Application name: flask-web-app
#### Project: default
#### Sync policy: Automatic
#### Repository URL: https://github.com/Rohit3Pandey/Flask-monitoring-app.git
#### Path: Deployment (This is the path to your "deplyment.yml" file which is consisted of all the configurations that will be used by Argo CD to deploy the application)  
#### Cluster URL: default Kubernetes cluster - https://kubernetes.default.svc
#### Namespace: default

### After the deployment of the application on Argo CD go to you terminal and run the following commands- 

```bash
minikube servive my-web-app --url 
```
the output of this command would be like this - http://127.0.0.1:50436 and you can use this to access your application on browser. 
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
![URL](https://github.com/Rohit3Pandey/Images/blob/main/Screenshot%20(102).png)

#### If you see something like this which is shown below than congrats, you have successfully deployed the web-app on kubernetes using Argo CD. 
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
![Flask-web-app](https://github.com/Rohit3Pandey/Images/blob/main/Screenshot%20(98).png)

# Challenges Encountered
Navigating the intricacies of Argo CD and orchestrating the deployment of a web application on Kubernetes presented a formidable challenge, particularly for someone approaching these technologies for the first time. In response, I diligently sought out resources and guidance, consulting the official documentation of Argo CD, leveraging insights from ChatGPT, and meticulously studying a variety of YouTube tutorials. Through these efforts, I gained invaluable insights into the nuances of crafting deployment YAML files and mastering essential practices, enabling me to execute the project with confidence and precision.

# Step 4: Documentation and Cleanup
### Clean Up
### To remove all resources created during this assignment from the Kubernetes cluster, follow these steps:

### Delete the Argo CD application:

```bash
kubectl delete application flask-web-app
```
### Delete the Argo CD namespace:

```bash
kubectl delete namespace argo
```
### Stop minikube

```bash
minikube stop
```
### Delete minikube

```bash
minikube delete
```

# Conclusion
By following this guide, you have successfully set up a GitOps pipeline with Argo CD for continuous deployment in a Kubernetes environment.



