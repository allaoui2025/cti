pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git url: 'https://github.com/allaoui2025/cti.git', credentialsId: 'github-token'
            }
        }

        stage('Build with Maven') {
            steps {
                sh 'mvn clean install'
            }
        }

         stage('🧠 Semgrep Scan (Code Analysis)') {
            steps {
                echo "🔍 Running Semgrep scan..."
                sh '''
                    pipx install semgrep || true
                    ~/.local/bin/semgrep --config auto .
                '''
            }
        }
        stage('Trivy Scan') {
            steps {
                sh 'trivy fs .'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying...'
            }
        }
    }
}
