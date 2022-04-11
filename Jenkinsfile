pipeline {
    agent any
    options { timestamps() }
    stages {
        stage('Stage_A') {
            steps {
                bat 'getjobstatus.py'
            }
        }
        stage('Stage_B') {
            steps {
                bat 'sleep.py'
            }
        }   
        stage('Stage_C') {
            steps {
                bat 'sleep1.py'
                bat "producer2.py"
            }
        }
    }
}
