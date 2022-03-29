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
                echo 'Deploying'
            }
        }
    }

    post {
        always {
            script{
                void printFinishedStageDurations() {
                    def visitor = new PipelineNodeGraphVisitor( currentBuild.rawBuild )
                    def stages = visitor.pipelineNodes.findAll{ it.type == FlowNodeWrapper.NodeType.STAGE }
                    for( stage in stages ) {
                        if( stage.node.endNode ) {   // only finished stages have endNode
                            def startTime  = TimingAction.getStartTime( stage.node )
                            def endTime    = TimingAction.getStartTime( stage.node.endNode )
                            def duration   = endTime - startTime
        
                            echo "Stage $stage.displayName duration: $duration ms" 
                        }
                    } 
                }
                printFinishedStageDurations()
            }
        }
    }
}
