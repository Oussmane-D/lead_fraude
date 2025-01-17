pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Récupérer le code depuis le dépôt
                git branch: 'main', url: 'https://github.com/Oussmane-D/lead_fraude.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    // Construire une image Docker à partir du Dockerfile
                    sh 'docker build -t ml-pipeline-image .'
                }
            }
        }

        stage('Install Dependencies') {
            steps {
                script {
                    // Tester l'installation des dépendances dans le conteneur
                    sh 'docker run --rm ml-pipeline-image python --version'
                }
            }
        }

        stage('Run Predictions') {
            steps {
                script {
                    // Exécuter le script principal pour les prédictions
                    sh 'docker run --rm ml-pipeline-image'
                }
            }
        }
    }

    post {
        always {
            echo 'Pipeline terminé.'
        }
        success {
            echo 'Pipeline exécuté avec succès !'
        }
        failure {
            echo 'Le pipeline a échoué.'
        }
    }
}
