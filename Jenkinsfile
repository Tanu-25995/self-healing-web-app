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

        stage('Test Application') {
            steps {
                sh '''
                    docker rm -f jenkins-test-app 2>/dev/null || true
                    docker run -d --name jenkins-test-app -p 5001:5000 self-healing-web-app
                    sleep 5
                    curl -f http://172.17.0.1:5001/health
                    docker rm -f jenkins-test-app
                '''
            }
        }
    }
}
