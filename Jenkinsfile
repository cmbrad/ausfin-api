pipeline {
    agent none

    stages {
        stage('test') {
            steps {
                sh '''
                python3.6 -m venv env
                . env/bin/activate
                pip install --upgrade pip setuptools

                pip install -r requirements.txt

                pytest
                '''

                stash includes: 'env/**/*', name: 'env'
            }
        }
        stage('package') {
            steps {
                unstash 'env'

                echo 'Hello, JDK'
                sh 'env/bin/zappa package api -o package.zip'

                stash includes: 'package.zip', name: 'package'
            }
        }
        stage('approve-deploy-prod') {
            steps {
                input message: 'Deploy?'
            }
        }
        stage('deploy-prod') {
            steps {
                unstash 'env'
                unstash 'package'

                echo "Install dependencies"
                sh 'env/bin/pip install awscli'

                echo "Uploading package to S3"
                sh "env/bin/aws s3 cp package.zip s3://cy-artefacts/ausfin-api/${BRANCH_NAME}/ausfin-api-${BUILD_NUMBER}.zip"

                echo "Executing database migrations"
                sh "env/bin/python manage.py migrate"

                echo "Deploying infrastructure"
                sh "terraform apply -var 'ausfin_api_artefact=ausfin-api/${BRANCH_NAME}/ausfin-api-${BUILD_NUMBER}.zip'"
            }
        }
    }
}
