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
				echo "${env.BUILD_NUMBER}"
				sh 'pip install pysimplegui'	
                sh 'python -m py_compile Main.py' 
				sh 'ls -l ; cat Main.py'
                stash(name: "${env.BUILD_NUMBER}", includes: 'Main.py*') 
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
                    unstash(name: "${env.BUILD_NUMBER}")
					sh "docker run --rm -v ${VOLUME} ${IMAGE} 'pwd; ls -l ; pyinstaller -F Main.py'"
					sh "echo 'LOOOOOOOL'"
					stash(name: "${env.BUILD_NUMBER}", includes: 'Main.*') 
					
                }
            }
            
        }
		stage('Upload') {
			agent any
			steps {
				dir("${env.BUILD_NUMBER}"){
				pwd()
				unstash "${env.BUILD_NUMBER}"
				
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
}