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
            }
        }
        stage('Stage_D') {
            steps {
                bat 'finaltimeExtarct1.py'
            }
        }    
    }
}
