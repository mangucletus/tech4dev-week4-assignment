# tech4dev-week4-assignment overview 

## Docker and Kubernetes Assignment

This repository contains the code and configurations for various tasks involving Docker and Kubernetes. The tasks include creating Dockerized applications, debugging broken configurations, integrating services, and deploying applications to Kubernetes. Each task is followed by a set of YAML configurations, Dockerfiles, and instructions for setting up and testing the services.

## Table of Contents
1. [Dockerized Flask Application](#dockerized-flask-application)
2. [Docker Compose Setup](#docker-compose-setup)
3. [Debugging Broken Docker Compose File](#debugging-broken-docker-compose-file)
4. [Kubernetes Challenges](#kubernetes-challenges)
    1. [Deploy a Simple Application](#deploy-a-simple-application)
    2. [Using ConfigMap and Secret](#using-configmap-and-secret)
    3. [Debug a Broken Kubernetes Configuration](#debug-a-broken-kubernetes-configuration)
5. [Advanced Docker and Kubernetes](#advanced-docker-and-kubernetes)
    1. [Docker and Kubernetes Integration](#docker-and-kubernetes-integration)

## Dockerized Flask Application

- **Objective**: Create a Dockerized Flask application, exposing it on port 5000.
- **Dockerfile**: Contains the instructions to build the Docker image.
- **Steps**: 
  - Create a Flask app that prints "Hello, Docker!".
  - Dockerize the app using a `Dockerfile`.
  - Build and run the Docker image.
  
## Docker Compose Setup

- **Objective**: Set up Docker Compose to run a Flask app alongside a Redis service.
- **docker-compose.yaml**: Defines the services for Flask and Redis.
- **Steps**: 
  - Flask app communicates with Redis.
  - Docker Compose configuration for the two services.

## Debugging Broken Docker Compose File

- **Objective**: Fix the errors in a broken Docker Compose configuration.
- **Steps**: 
  - Correct the indentation and syntax issues.
  - Fix the service definitions and ensure proper communication between the services.

## Kubernetes Challenges

### Deploy a Simple Application

- **Objective**: Deploy an nginx application with 3 replicas in Kubernetes.
- **YAML Files**: Includes `Deployment` and `Service` configurations.
- **Steps**: 
  - Create a Kubernetes deployment for nginx.
  - Expose the application using a `ClusterIP` service.

### Using ConfigMap and Secret

- **Objective**: Pass environment variables using a ConfigMap and a Secret.
- **YAML Files**: ConfigMap for `app-color` and Secret for `api-key`.
- **Steps**:
  - Create a `ConfigMap` and `Secret` to store key-value pairs.
  - Modify the Deployment to use these environment variables.

### Debug a Broken Kubernetes Configuration

- **Objective**: Fix errors in a broken Kubernetes Deployment configuration.
- **Steps**:
  - Correct label mismatches and indentation errors to ensure proper pod management.

## Advanced Docker and Kubernetes

### Docker and Kubernetes Integration

- **Objective**: Deploy a Flask application in Kubernetes, expose it via a LoadBalancer service, and pass an environment variable using a ConfigMap.
- **Dockerfile**: The same Dockerfile used for the Flask application.
- **YAML Files**: 
  - `Deployment`: For deploying the Flask application.
  - `Service`: A LoadBalancer service to expose the application.
  - `ConfigMap`: For passing the `WELCOME_MSG` environment variable.
- **Steps**:
  - Create and push a Docker image for the Flask app.
  - Deploy the app in Kubernetes and expose it via a LoadBalancer.
  - Set up a ConfigMap to pass environment variables to the application.

## How to Run

1. **Build Docker Image**:
   ```bash
   docker build -t yourusername/flask-app:latest .
