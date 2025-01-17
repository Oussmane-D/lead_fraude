pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/Oussmane-D/lead_fraude.git'
            }
        }
        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Run Predictions') {
            steps {
                sh 'python scripts/main.py'
            }
        }
    }
}