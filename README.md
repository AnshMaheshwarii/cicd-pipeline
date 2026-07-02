# CI/CD Pipeline Automation Project

A full CI/CD pipeline built around a Flask app using Jenkins, Docker, Amazon ECR, Amazon ECS (Fargate), Terraform, and AWS.

The goal wasn't just to containerize something — it was to actually understand how a modern deployment pipeline works from source code all the way to a running app in the cloud.

**Repo:** [github.com/AnshMaheshwarii/cicd-pipeline](https://github.com/AnshMaheshwarii/cicd-pipeline)

> Note: AWS resources (ECS, ECR, Fargate) aren't kept running permanently since that eats into credits. Screenshots of the full pipeline, deployments, and AWS infrastructure are in the `/screenshots` folder in the repo.

## What the pipeline does

Once triggered, it automatically:

- Builds the app
- Runs automated tests (if tests fail, deployment stops)
- Builds a Docker image
- Pushes it to Amazon ECR
- Deploys the latest image to Amazon ECS

Jenkins runs locally on my machine, so the pipeline is kicked off manually for now. In a real production setup this would be triggered automatically via GitHub Webhooks on a hosted Jenkins server.

## Pipeline flow

```text
Developer
    │
  Git Push
    │
    ▼
  Jenkins
    │
    ▼
  Pytest
    │
    ▼
Docker Build
    │
    ▼
Amazon ECR
    │
    ▼
Amazon ECS → AWS Fargate → Live App
```

## Architecture

```text
GitHub (source code)
    │
    ▼
Jenkins CI
    │
    ├── Install Dependencies
    ├── Run Tests (Pytest)
    ├── Docker Build
    │
    ▼
Amazon ECR
    │
    ▼
Amazon ECS Service → Fargate Tasks → Flask Web App
```

## Stack

**Backend**
- Python + Flask

**Testing**
- Pytest

**Containerization**
- Docker

**CI/CD**
- Jenkins

**Infrastructure as Code**
- Terraform

**AWS**
- Amazon ECS, ECR, Fargate, IAM

**Version Control**
- Git + GitHub

## Project structure

```text
cicd-pipeline/
├── screenshots/
├── static/
├── templates/
├── terraform/
├── tests/
├── app.py
├── Dockerfile
├── Jenkinsfile
├── requirements.txt
├── requirements-dev.txt
├── .dockerignore
├── .gitignore
└── README.md
```

## Pipeline stages

**Stage 1 — Environment check**
Validates Git, Python, Java, Docker, and AWS CLI are all present and working.

**Stage 2 — Checkout**
Pulls the latest source code from GitHub.

**Stage 3 — Install dependencies**
```bash
pip install -r requirements.txt
```

**Stage 4 — Run tests**
```bash
pytest
```
If anything fails here, the pipeline stops. No broken code gets deployed.

**Stage 5 — Docker build**
```bash
docker build -t cicd-dashboard .
```

**Stage 6 — ECR auth + push**
Authenticates with Amazon ECR and pushes the freshly built image.

**Stage 7 — ECS deployment**
```bash
aws ecs update-service --force-new-deployment
```
ECS pulls the latest image and does a rolling deployment.

## Terraform

Used Terraform to get comfortable with Infrastructure as Code — provisioning an S3 bucket, going through the init → plan → apply → destroy workflow. Nothing massive, but it clicked a lot of things into place.

## Running it locally

```bash
git clone https://github.com/AnshMaheshwarii/cicd-pipeline.git
pip install -r requirements.txt
pip install -r requirements-dev.txt
python app.py        # run the app
pytest               # run tests
docker build -t cicd-dashboard .   # build the image
```

## Screenshots

All screenshots are in the `/screenshots` folder — Jenkins pipeline runs, Docker images, ECR, ECS tasks, Terraform, the whole setup. Check there if you want to see it in action.

## Challenges I actually ran into

Not everything worked first try — some of the real issues I had to debug:

- Jenkins config on Windows (painful)
- AWS CLI integration inside Jenkins
- Secure credential management without hardcoding keys
- ECS Task Execution Role permissions
- IAM permission issues
- Terraform state management
- ECR authentication
- Windows PATH config breaking things

Sorting these out taught me more than any tutorial would've.

## What I learned

- Designing CI/CD pipelines end to end
- Docker image lifecycle management
- Jenkins Declarative Pipelines
- Deploying containers on AWS ECS + Fargate
- IaC with Terraform
- IAM roles and permissions
- ECS rolling deployments
- Actually debugging real cloud deployment issues

## About me

**Ansh Maheshwarii** — focused on cloud, DevOps, and infrastructure. Building projects like this instead of just grinding tutorials.

GitHub: [github.com/AnshMaheshwarii](https://github.com/AnshMaheshwarii)
