pipeline {
    agent any
    stages {
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
                sh 'source venv/bin/activate'
            }
        }
    }
}