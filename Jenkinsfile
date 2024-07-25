pipeline{
    agent any
    stages{
         stage("GitHub checking checkout....") {
            steps {
                script {
 
                    git branch: 'main', url:  'https://github.com/paulfatoki/python_flask_app2.git'
                }
            }
        }
        stage("Building docker on going"){
            steps{
                sh 'printenv'
                sh 'git version'
                sh 'docker build . -t paulfatoki/imag2.0'
            }
        }
         stage("pushing image to DockerHub"){
            steps{

               script {
                  
                 withCredentials([string(credentialsId: 'dockerid', variable: 'dockerid')]) {
                    sh 'docker login -u paulfatoki -p ${dockerid}'
            }
              sh 'docker push paulfatoki/imag2.0:latest'
            }
        }
    }
    }
}
