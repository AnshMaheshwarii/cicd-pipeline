pipeline {
    agent any

    stages {

        stage('Environment Check') {
            steps {
                bat 'git --version'
                bat '"C:\\Users\\anshk\\AppData\\Local\\Programs\\Python\\Python312\\python.exe" --version'
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
                bat '"C:\\Users\\anshk\\AppData\\Local\\Programs\\Python\\Python312\\python.exe" -m pip install -r requirements.txt'
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

    }

    post {
        success {
            echo '🎉 Pipeline completed successfully!'
        }

        failure {
            echo '❌ Pipeline failed.'
        }

        always {
            echo 'Pipeline execution finished.'
        }
    }
}