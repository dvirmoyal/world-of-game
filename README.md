# Python Application with CI/CD Pipeline and Bitnami MySQL Integration

## Table of Contents
1. [Project Overview](#project-overview)
2. [Repository Structure](#repository-structure)
3. [Architecture](#architecture)
4. [Features](#features)
5. [Prerequisites](#prerequisites)
6. [Database Configuration](#database-configuration)
7. [Setup Instructions](#setup-instructions)
8. [Security Considerations](#security-considerations)
9. [Troubleshooting Guide](#troubleshooting-guide)
10. [Contributing](#contributing)

## Project Overview
This project demonstrates a complete CI/CD pipeline implementation using GitHub Actions for CI and a self-hosted runner for CD, deploying a Python Flask application with Bitnami MySQL integration. The pipeline includes automated building, testing, containerization, and deployment processes with secure credentials management and database initialization.

## Repository Structure
```
.
├── .github/
│   └── workflows/          # CI/CD Pipeline definitions
├── my-chart/              # Helm Chart for deployment
│   ├── templates/
│   │   ├── _helpers.tpl
│   │   ├── flask-app-deployment.yaml
│   │   ├── flask-app-service.yaml
│   │   ├── mysql-init-configmap.yaml
│   │   └── secrets-dev.yaml
│   ├── Chart.yaml         # Chart dependencies
│   └── values.yaml        # Default configuration
├── .idea/                 # IDE configuration
├── .cz.toml              # Commitizen configuration
├── .gitignore            # Git ignore rules
├── .pre-commit-config.yaml # Pre-commit hooks
├── Dockerfile            # Application containerization
├── MainGame.py           # Game logic
├── app.py               # Flask application
├── live.py              # Live environment configuration
└── README.md            # Project documentation
```

## Architecture

### Overall System Architecture
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

[Previous sections about Features, Prerequisites, etc. remain the same...]

## Database Configuration

### MySQL Initialization
```yaml
# mysql-init-configmap.yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: {{ .Release.Name }}-mysql-init-scripts
data:
  give_root_access.sql: |
    ALTER USER 'root'@'%' IDENTIFIED WITH mysql_native_password BY 'root';
    GRANT ALL PRIVILEGES ON *.* TO 'root'@'%' WITH GRANT OPTION;
    FLUSH PRIVILEGES;
```

### Database Integration Flow
```mermaid
graph LR
    A[Init Container] -->|Executes| B[ConfigMap Script]
    B -->|Configures| C[MySQL Server]
    D[Flask App] -->|Connects as root| C
    C -->|Full Access| E[Database Operations]
    style A fill:#228B22
    style B fill:#B22222
    style C fill:#800080
    style D fill:#4169E1
    style E fill:#006400
```

[Rest of the content remains the same...]