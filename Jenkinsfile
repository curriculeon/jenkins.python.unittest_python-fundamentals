pipeline {
  agent { any }
  stages {
    stage('build') {
      steps {
        sh 'pip3 install -r requirements.txt'
      }
    }
    stage('test') {
      steps {
        sh 'python3 -m unittest discover -s ./src/test/ -p '*_test.py''
      }   
    }
  }
}