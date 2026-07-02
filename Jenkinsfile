pipeline {
    agent any

    environment {
        AWS_REGION = 'ap-south-1'
        AWS_ACCOUNT_ID = '323960980728'
        ECR_REPO = 'cicd-dashboard'
        IMAGE_TAG = 'latest'
    }

    stages {

        stage('Environment Check') {
            steps {
                bat 'git --version'
                bat '"C:\\Users\\anshk\\AppData\\Local\\Programs\\Python\\Python312\\python.exe" --version'
                bat 'java -version'
                bat 'docker --version'
                bat 'aws --version'
            }
        }

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                bat '"C:\\Users\\anshk\\AppData\\Local\\Programs\\Python\\Python312\\python.exe" -m pip install -r requirements.txt'
                bat '"C:\\Users\\anshk\\AppData\\Local\\Programs\\Python\\Python312\\python.exe" -m pip install -r requirements-dev.txt'
            }
        }

        stage('Run Tests') {
            steps {
                bat '"C:\\Users\\anshk\\AppData\\Local\\Programs\\Python\\Python312\\python.exe" -m pytest'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t cicd-dashboard .'
            }
        }

        stage('Push to Amazon ECR') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'aws-creds',
                    usernameVariable: 'AWS_ACCESS_KEY_ID',
                    passwordVariable: 'AWS_SECRET_ACCESS_KEY'
                )]) {

                    bat '''
                    aws ecr get-login-password --region %AWS_REGION% | docker login --username AWS --password-stdin %AWS_ACCOUNT_ID%.dkr.ecr.%AWS_REGION%.amazonaws.com

                    docker tag cicd-dashboard:latest %AWS_ACCOUNT_ID%.dkr.ecr.%AWS_REGION%.amazonaws.com/%ECR_REPO%:%IMAGE_TAG%

                    docker push %AWS_ACCOUNT_ID%.dkr.ecr.%AWS_REGION%.amazonaws.com/%ECR_REPO%:%IMAGE_TAG%
                    '''
                }
            }
        }
    }
stage('Deploy to ECS') {
    steps {
        withCredentials([usernamePassword(
            credentialsId: 'aws-creds',
            usernameVariable: 'AWS_ACCESS_KEY_ID',
            passwordVariable: 'AWS_SECRET_ACCESS_KEY'
        )]) {

            bat '''
            aws ecs update-service ^
              --cluster test-cluster ^
              --service cicd-dashboard-service ^
              --force-new-deployment ^
              --region %AWS_REGION%
            '''
        }
    }
}
    post {
        success {
            echo 'Pipeline completed successfully!'
        }

        failure {
            echo 'Pipeline failed.'
        }

        always {
            echo 'Pipeline execution finished.'
        }
    }
}