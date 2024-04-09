# Flask-Monitoring-Application
# GitOps with Argo CD

## Project Overview

The aim of this assignment is to understand the hands-on experience with GitOps practices, utilizing Argo CD for continuous deployment and Argo Rollouts for advanced deployment strategies within a Kubernetes environment. You will be responsible for setting up a GitOps pipeline that automates the deployment and management of a simple web application.

### Application Overview

Our application is a simple web application that displays system metrics such as CPU utilization and memory usage. It is built using Python Flask and utilizes the psutil library to collect system metrics. The application serves a single-page HTML template using Flask's render_template function.

### Prerequisites

Before getting started, ensure you have the following prerequisites installed:

- Docker Desktop
- Git Bash

## Step-by-Step Guide

### Step 1: Install Minikube Locally

- Download and install Minikube locally using the following command:

```bash
Invoke-WebRequest -OutFile 'c:\minikube\minikube.exe' -Uri 'https://github.com/kubernetes/minikube/releases/latest/download/minikube-windows-amd64.exe' -UseBasicParsing
New-Item -Path 'c:\' -Name 'minikube' -ItemType Directory -Force
minikube start

Verify that Minikube is running:

minikube status
