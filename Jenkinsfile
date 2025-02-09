pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'devopsbook-web'
        DOCKER_TAG = 'latest'
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/muraasra/devopsbook.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    bat """
                    docker build -t ${DOCKER_IMAGE}:${DOCKER_TAG} .
                    """
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    bat """
                    docker run --rm ${DOCKER_IMAGE}:${DOCKER_TAG} python manage.py test
                    """
                }
            }
        }

        stage('Deploy Locally') {
            steps {
                script {
                    bat """
                    docker-compose down || exit 0
                    docker-compose up -d
                    """
                }
            }
        }
    }

    post {
        success {
            echo 'Pipeline terminé avec succès !'
        }
        failure {
            echo 'Pipeline échoué.'
        }
    }
}