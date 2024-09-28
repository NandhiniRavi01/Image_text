pipeline {
    agent any

   stages {
        stage('Checkout') {
            steps {
                git credentialsId: 'git-credential', 
                    url: 'https://github.com/NandhiniRavi01/Image_text.git',
                    branch: 'main'
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
