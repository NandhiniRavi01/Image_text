pipeline {
    agent any

    stages {
        stage('Expose Jenkins with Ngrok') {
            steps {
                script {
                    sh 'nohup ngrok http 8080 &'
                }
            }
        }
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/NandhiniRavi01/Image_text.git'
            }
        }
        stage('Build Docker Image') {
            steps {
                script {
                    echo 'Building Docker Image'
                    sh 'docker build -t flask-ocr-app:latest .'
                }
            }
        }
        stage('Cleanup Docker') {
            steps {
                script {
                    echo 'Cleaning up old Docker containers'
                    sh 'docker rm -f flask-ocr-app || true'
                    sh 'docker container prune -f'
                }
            }
        }
        stage('Check and Free Port') {
            steps {
                script {
                    echo 'Checking and freeing port 5000 if in use'
                    sh "sudo fuser -k 5000/tcp || true"
                }
            }
        }
        stage('Run Docker Container') {
            steps {
                script {
                    echo 'Running Docker Container'
                    sh 'docker run -d --name flask-ocr-app -p 5000:5000 flask-ocr-app:latest'
                    sleep 20
                    sh 'docker exec flask-ocr-app pip show flask'
                    sh 'docker exec flask-ocr-app ls'
                }
            }
        }
    }
    post {
        always {
            script {
                echo 'Cleaning up...'
                sh 'docker stop flask-ocr-app || true'
                sh 'docker rm flask-ocr-app || true'
            }
        }
    }
}
