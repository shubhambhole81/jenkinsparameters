pipeline {
    agent any
    options { timestamps() }
    stages {
        stage('Stage_D') {
            steps {
                bat 'script1.py'
            }
        }
        stage('Stage_E') {
            steps {
                bat 'script2.py'
            }
        }
    }
}
