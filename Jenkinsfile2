pipeline {
    agent any
    options { timestamps() }
    stages {
        stage('Stage_D') {
            steps {
                bat 'getjobstatus.py'
            }
        }
        stage('Stage_E') {
            steps {
                bat 'sleep.py'
            }
        }
        stage('Stage_F') {
            steps {
                bat 'sleep1.py'
            }
        }
    }
}
