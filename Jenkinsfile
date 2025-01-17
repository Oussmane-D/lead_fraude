pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/Oussmane-D/lead_fraude.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t fraud-detection-image .'
            }
        }

        stage('Train Model') {
            steps {
                sh 'docker run --rm fraud-detection-image python data/train_model.py'
            }
        }

        stage('Run Predictions') {
            steps {
                sh 'docker run --rm fraud-detection-image python scripts/predict.py'
            }
        }
    }

    post {
        success {
            echo 'Pipeline exécuté avec succès !'
        }
        failure {
            echo 'Le pipeline a échoué.'
        }
    }
}
