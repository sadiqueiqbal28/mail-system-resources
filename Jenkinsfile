pipeline {
    agent any
    stages {
        stage ('Clean Workspace') {
            steps {
                cleanWs()
            }
        }
        stage ('Print Hello World') {
            steps {
                sh 'echo "Hello World"'
            }
        }
        stage ('Create Virtual Environment') {
            steps {
                sh 'python -m venv venv'
            }
        }
        stage ('Activate Virutal Environment') {
            steps {
                sh '. venv/bin/activate'
            }
        }
        stage ('List down pip packages') {
            steps {
                sh 'pip list'
            }
        }
        stage ('Clean Workspace at last') {
            steps {
                cleanWs()
            }
        }
    }
}