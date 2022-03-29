import jenkins.model.*
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
                    modules.buildstatus = load ("buildstatus.groovy")
                    module.buildstatus.printFinishedStageDurations()
                    echo 'Deploying'
                    bat "getjobstatus.py"
                }    
            }
        }
    }
}  
