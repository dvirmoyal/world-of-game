.. dvir-Portfolio documentation master file, created by
   sphinx-quickstart on Sat Dec 21 13:47:12 2024.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

===============================
DevOps & AWS Portfolio
===============================

Welcome to my technical portfolio! Here you'll find detailed documentation of my projects in DevOps and AWS Cloud Architecture.

.. toctree::
   :maxdepth: 1
   :caption: Navigation
   :hidden:

   projects/devops-project
   projects/aws-architecture
   skills/technical-skills
   about/experience

CI/CD Pipeline with Kubernetes
-----------------------------

.. figure:: _static/ci-cd-diagram.png
   :align: center
   :alt: CI/CD Diagram
   :width: 600px

   **Enterprise CI/CD Pipeline with GitOps Methodology**

An advanced DevOps implementation showcasing:

1. **Semantic Versioning** for reliable artifact management using GitHub Actions
2. **GitOps Deployments** with ArgoCD and Image Updater
3. **HELM Chart Management** for streamlined Kubernetes package deployment
4. **HashiCorp Vault** for enterprise-grade secrets management
5. **Centralized Monitoring** with Grafana and CloudWatch
6. **Infrastructure as Code** with Terraform on AWS
7. **Kubernetes Cluster Orchestration** and management

This flexible CI/CD pipeline has also been successfully implemented for a **Java-based application**, proving its adaptability to various programming languages and environments.

- Java CI process repository: `Java CI Repository <https://github.com/dvirmoyal/dvir-java-app-ci.git>`_
- Java CD process repository: `Java CD Repository <https://github.com/dvirmoyal/java-app-cd.git>`_

For detailed explanations and full code, please visit the main repository:
`World of Game Repository <https://github.com/dvirmoyal/world-of-game.git>`_

`Read Full Technical Details - CI/CD » <projects/devops-project.html>`_



AWS Cloud Architecture
----------------------

.. figure:: _static/aws-architecture-diagram.png
   :align: center
   :alt: AWS Architecture Diagram
   :width: 600px


An advanced AWS cloud architecture implementation showcasing:

1. **Static Content Delivery with CloudFront (CF):**
   - Leveraging CloudFront to efficiently deliver static content to users at high speeds.
   - Using CloudFront's Origin feature to route API requests to the Application Load Balancer (ALB) using the `/api` path.

2. **Secure Routing with CloudFront:**
   - Using HTTP headers in the requests passed through CloudFront to the ALB to authenticate that the requests are originating from CloudFront.
   - Ensuring that only authorized requests reach the application, enhancing overall security.

3. **Automated Updates to Auto Scaling Groups (ASG):**
   - Implementing a CI/CD process that uses Packer to automatically create new EC2 machine images.
   - The new images update the Launch Template of the ASG, enabling automated updates to the environment.
   - A creative and advanced solution to ensure rapid upgrades and stabilization of the environment.

`Read Full Technical Details - AWS » <projects/aws-architecture.html>`_


