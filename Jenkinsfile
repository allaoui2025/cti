pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/your/repo.git'
            }
        }

        stage('Build with Maven') {
            steps {
                sh 'mvn clean install'
            }
        }

        stage('Static Analysis - Semgrep') {
            steps {
                sh 'semgrep --config=auto .'
            }
        }

        stage('Trivy Scan') {
            steps {
                sh 'docker build -t myapp .'
                sh 'trivy image myapp'
            }
        }

        stage('Deploy') {
            steps {
                sh 'docker run -d -p 9090:8080 myapp'
            }
        }
    }
}
