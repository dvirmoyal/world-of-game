=================================
AWS Cloud Architecture Overview
=================================

This page provides an in-depth look into the advanced AWS cloud architecture implementation.

Overview
--------

The architecture is designed to deliver high scalability, security, and performance while minimizing costs.

**Key Features:**

1. **Static Content Delivery with CloudFront:**
   - Deliver static content (e.g., images, CSS, JavaScript) efficiently using AWS CloudFront.
   - Utilize CloudFront's caching mechanism to reduce latency and improve user experience.

2. **Secure API Routing:**
   - API requests are routed through CloudFront to an Application Load Balancer (ALB).
   - HTTP headers are used to authenticate that requests originate from CloudFront, ensuring security.

3. **Automated Scaling with ASG:**
   - Auto Scaling Groups (ASG) automatically adjust the number of EC2 instances based on traffic.
   - Updates to instances are managed with Packer to create AMIs and update Launch Templates.

Architecture Diagram
--------------------

.. figure:: ../_static/aws-architecture-diagram.png
   :align: center
   :alt: AWS Architecture Diagram
   :width: 600px



Workflow Steps
--------------

1. **Static Content:**
   - Hosted on S3 and served through CloudFront.
   - Leverages CloudFront caching for reduced latency.

2. **Dynamic API Requests:**
   - Passed through CloudFront and routed to the ALB.
   - ALB forwards requests to the appropriate backend EC2 instances.

3. **Continuous Deployment:**
   - Packer automates the creation of machine images.
   - CI/CD pipelines update the ASG's Launch Template with new AMIs.

Tools and Technologies
----------------------

- **CloudFront**
- **Application Load Balancer**
- **Auto Scaling Groups**
- **Amazon S3**
- **Packer**
- **CI/CD Pipelines**





