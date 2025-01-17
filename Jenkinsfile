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
                sh 'python3 --version'  // Vérifie la version de Python 3
                sh 'pip3 --version'  // Vérifie la version de pip3
            }
        }
        stage('Install Dependencies') {
            steps {
                sh 'pip3 install -r requirements.txt'  // Installe les dépendances
            }
        }
        stage('Run Predictions') {
            steps {
                sh 'python3 scripts/main.py'  // Exécute le script principal
            }
        }
    }
}
