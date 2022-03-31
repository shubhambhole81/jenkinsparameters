pipeline {
    agent any
    options { timestamp() }
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
                echo 'Deploying'
            }
        }
    }
}
