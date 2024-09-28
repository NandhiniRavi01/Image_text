pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                script {
                    // Pull the latest code from the repository
                    git 'https://github.com/NandhiniRavi01/your-repo.git'
                    
                    // Build the Docker image
                    sh 'docker build -t flask-ocr-app .'
                }
            }
        }

        stage('Deploy') {
            steps {
                script {
                    // Stop and remove any existing container
                    sh 'docker rm -f flask-ocr-app || true'
                    
                    // Run the new container
                    sh 'docker run -d -p 5000:5000 --name flask-ocr-app flask-ocr-app'
                }
            }
        }
    }

    post {
        always {
            // Cleanup actions (optional)
            echo 'Cleanup after build...'
        }
    }
}
