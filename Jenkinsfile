pipeline {
    agent any

    stages {

        stage('Environment Check') {
            steps {
                bat 'git --version'
                bat 'python --version'
                bat 'java -version'
                bat 'docker --version'
            }
        }

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'python -m pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                bat 'pytest'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t cicd-dashboard .'
            }
        }
    }
}