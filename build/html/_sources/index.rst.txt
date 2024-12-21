.. dvir-Portfolio documentation master file, created by
   sphinx-quickstart on Sat Dec 21 13:47:12 2024.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

===============================
DevOps & AWS Portfolio
===============================

Welcome to my technical portfolio! Here you'll find detailed documentation of my projects in DevOps and AWS Cloud Architecture.

.. toctree::
   :maxdepth: 2
   :caption: Navigation

   projects/devops-project
   projects/aws-architecture
   skills/technical-skills
   about/experience

CI/CD Pipeline with Kubernetes
-----------------------------

.. figure:: _static/ci-cd-arch.png
   :align: center
   :alt: CI/CD Architecture Diagram
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

`Read Full Technical Details » <projects/devops-project.html>`_

AWS Cloud Architecture
----------------------

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

`Read Full Technical Details » <projects/aws-architecture.html>`_

