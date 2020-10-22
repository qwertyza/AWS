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
				sh 'ls -l ; cat Main.py'
                stash(name: 'compiled-results', includes: 'Main.py*') 
            }
        }
		stage('Deliver') {
            agent any
            environment {
                VOLUME = '$HOME:/src'
                IMAGE = 'cdrx/pyinstaller-linux:python2'
            }
            steps {
                dir(path: env.BUILD_ID) {
                    unstash(name: 'compiled-results')
					sh "docker run --rm -v ${VOLUME} ${IMAGE} 'pwd; ls -l ; pyinstaller -F Main.py'"
					
                }
            }
            
        }
		
    }
}