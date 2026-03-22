pipeline {
    agent any

    stages {
        stage('Clone Code') {
            steps {
                git 'https://github.com/Vishal-AWS-Devops/devops-project.git'
            }
        }

        stage('Deploy with Docker Compose') {
            steps {
                sh 'docker compose down || true'
                sh 'docker compose up -d --build'
            }
        }

        stage('Cleanup') {
            steps {
                sh 'docker system prune -f'
            }
        }
    }
}
