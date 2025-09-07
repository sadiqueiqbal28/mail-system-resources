pipeline {
    agent any

    environment {
        SENDER_EMAIL=credentials('SENDER_EMAIL')
        RECEIVER_EMAIL=credentials('RECEIVER_EMAIL')
        APP_PASSWORD=credentials('APP_PASSWORD')
    }

    // This part of code disables Jenkins default checkout
    options {
        skipDefaultCheckout(true)
    }

    stages {

        stage ('Clean Workspace') {
            steps {
                cleanWs()
            }
        }

        stage('Checkout repository') {
            steps {
                checkout SCM
            }
        }

        stage ('Create Virtual Environment') {
            steps {
                sh 'python -m venv venv'
            }
        }

        stage ('Install dependencies') {
            steps {
                sh 'venv/bin/python -r requirements.txt'
            }
        }

        stage ('Execute Python Mail script') {
            steps {
                sh 'venv/bin/python main.py'
            }
        }

        stage ('Clean Workspace at last') {
            steps {
                cleanWs()
            }
        }
    }
}