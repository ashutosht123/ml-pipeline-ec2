pipeline {
    agent any

    environment {
        EC2_USER = "ubuntu"
        EC2_HOST = "<your-ec2-public-ip>"
        SSH_KEY = "C:\\Users\\your_user\\.ssh\\id_rsa"
    }

    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main', url: "git@github.com:yourusername/yourrepo.git"
            }
        }

        stage('Setup Environment') {
            steps {
                bat 'pip install -r requirements.txt'
            }
        }

        stage('Train Model') {
            steps {
                bat 'python train.py'
            }
        }

        stage('Deploy Model to EC2') {
            steps {
                bat '''
                scp -i "%SSH_KEY%" model.pkl %EC2_USER%@%EC2_HOST%:/home/ubuntu/deployed_model.pkl
                ssh -i "%SSH_KEY%" %EC2_USER%@%EC2_HOST% "sudo systemctl restart ml-service"
                '''
            }
        }
    }
}
