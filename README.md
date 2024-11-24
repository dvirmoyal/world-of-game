# Python Application with CI/CD Pipeline and Bitnami MySQL Integration

## Project Overview
This project implements a CI/CD pipeline using GitHub Actions (CI) and a self-hosted runner (CD), deploying a Python Flask application with Bitnami MySQL integration. The pipeline automates building, testing, containerization, and deployment processes.

## Architecture

### System Flow
```mermaid
graph TB
    subgraph "CI Process (Cloud Runner)"
        A[Python App] --> B[Docker Build]
        B --> C[Push to GHCR]
        style A fill:#228B22
        style B fill:#1E90FF
        style C fill:#DC143C
    end
    subgraph "CD Process (Self-Hosted Runner)"
        D[Pull from GHCR] --> E[Helm Deploy]
        style D fill:#8B008B
        style E fill:#DAA520
    end
    subgraph "Application Stack"
        F[LoadBalancer] --> G[Flask App Service]
        G --> H[Flask App Pod]
        H --> I[MySQL Service]
        I --> J[Bitnami MySQL]
        J --> K[Init ConfigMap]
        style F fill:#006400
        style G fill:#8B4513
        style H fill:#228B22
        style I fill:#4169E1
        style J fill:#B22222
        style K fill:#800080
    end
    subgraph "Secrets & Configuration"
        L[Registry Secret]
        M[MySQL Root Secret]
        N[MySQL User Secret]
        style L fill:#CD853F
        style M fill:#CD853F
        style N fill:#CD853F
    end
    C --> D
    E --> G
    H --> L
    J --> M
    J --> N
```

## Key Features

### Bitnami MySQL Integration
- Simplified deployment using Helm chart
- Reduced YAML configuration (from 400+ lines to ~10 lines)
- Built-in monitoring, backup, and security features

### CI/CD Pipeline
- **CI**: Automated builds, tests, and Docker image publishing
- **CD**: Self-hosted runner for controlled deployments
- Secure credentials management

## Prerequisites
- GitHub account and repository access
- Docker
- Kubernetes cluster
- Helm 3.x
- Self-hosted runner
- GHCR access

## Quick Start

### 1. Setup Repository
```bash
git clone <repository-url>
cd <repository-name>
# Add GITHUB_TOKEN and PAT_GHCR secrets in GitHub
```

### 2. Configure Database
```bash
# Create secrets
kubectl create secret generic mysql-credentials \
  --from-literal=root-password=<root-password> \
  --from-literal=user-password=<user-password> \
  -n dvir-app

# Deploy with Helm
helm dependency update ./my-chart
helm upgrade -i my-app-dev ./my-chart \
  --namespace dvir-app \
  --set mysql.auth.rootPassword="${MYSQL_ROOT_PASSWORD}"
```

### 3. Verify Deployment
```bash
kubectl get pods,svc -n dvir-app
```

## Troubleshooting Guide

### Quick Checks
```bash
# CI Issues
- Check GitHub Actions logs
- Verify Docker build locally

# CD Issues
- Check runner status: gh runner list
- Verify Helm: helm list -n dvir-app

# Application Issues
kubectl logs -f <pod-name> -n dvir-app
kubectl get all -n dvir-app

# Database Issues
kubectl logs -f <mysql-pod> -n dvir-app
kubectl exec -it <mysql-pod> -n dvir-app -- \
  mysql -u root -p<password> -e "SHOW DATABASES;"
```

## Security Notes
- Development: Root access enabled for simplicity
- Production: Use restricted users and enable SSL/TLS

## Contributing
1. Fork repository
2. Create feature branch
3. Submit pull request

---



