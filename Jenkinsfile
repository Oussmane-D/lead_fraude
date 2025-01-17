pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/Oussmane-D/lead_fraude.git'
            }
        }
        stage('Debug') {
            steps {
                sh 'pwd'  // Affiche le répertoire de travail
                sh 'ls -la'  // Liste les fichiers dans le répertoire
                sh 'python --version'  // Vérifie la version de Python
                sh 'pip --version'  // Vérifie la version de pip
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