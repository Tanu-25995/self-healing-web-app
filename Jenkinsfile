
pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/Tanu-25995/self-healing-web-app.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t self-healing-web-app .'
            }
        }
    }
}
