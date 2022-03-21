pipeline {
  agent any
  stages {
    stage('Test') {
      steps {
        sh 'whoami'
      }
    }

    stage('Update') {
      steps {
        sh 'apt update'
      }
    }

  }
}