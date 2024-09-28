pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'flask-ocr-app:latest'
        CONTAINER_NAME = 'flask-ocr-app'
        DOCKER_HUB_USER = credentials('docker-credentials')  // Replace with your Jenkins credentials ID for Docker Hub
    }

    stages {
        stage('Checkout Code') {
            steps {
                git url: 'https://github.com/your-repo/flask-ocr-app.git', branch: 'main'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    dockerImage = docker.build("${DOCKER_IMAGE}")
                }
            }
        }

        stage('Clean Up Old Containers') {
            steps {
                script {
                    // Stop and remove the old container if it exists
                    sh """
                    docker stop ${CONTAINER_NAME} || true
                    docker rm ${CONTAINER_NAME} || true
                    """
                }
            }
        }

        stage('Run Docker Container') {
            steps {
                script {
                    // Run the newly built container
                    sh """
                    docker run -d -p 5000:5000 --name ${CONTAINER_NAME} ${DOCKER_IMAGE}
                    """
                }
            }
        }

        stage('Post-deployment') {
            steps {
                echo 'Deployment complete. Flask app with OCR is running.'
            }
        }
    }

    post {
        always {
            cleanWs()
        }
    }
}
