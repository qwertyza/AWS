pipeline {
    agent none 
    stages {
        stage('Build') { 
            agent {
                docker {
                    image 'python:2-alpine' 
                }
            }
            steps {
				sh 'pip install pysimplegui'	
                sh 'python -m py_compile Main.py' 
                stash(name: 'compiled-results', includes: 'sources/*.py*') 
            }
        }
    }
}