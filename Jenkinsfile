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
                stash(name: '${env.BUILD_ID}', includes: 'Main.py*') 
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
		stage('Upload') {
			agent any
			steps {
				pwd()
				unstash "${env.BUILD_ID}"
				script {
						withAWS(region:'eu-west-1',credentials:'AWSfromJenkins') {
						 def identity=awsIdentity()

						sh 'ls -l ; pwd'
						s3Upload(bucket:"okulaginide", includePathPattern:'**/*')
						}
				}
			}
		}
    }
}