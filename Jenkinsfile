def modules = [:]
pipeline {
    agent any
    stages {
        stage('Stage_A') {
            steps {
                echo 'Building'
            }
        }
        stage('Stage_B') {
            steps {
                echo 'Testing'
            }
        }   
        stage('Stage_C') {
            steps {
                 script{
                    modules.first = load ("")
                    echo 'Deploying'
                    bat "getjobstatus.py"
            }
        }
    }
}  
