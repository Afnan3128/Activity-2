pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                // Checkout the source code from the Git repository
                git 'https://github.com/yourusername/your-repo.git'
            }
        }
        stage('Install Dependencies') {
            steps {
                // Install Python dependencies using requirements.txt
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Run Tests') {
            steps {
                // Run tests using pytest (replace with your test command)
                sh 'pytest'
            }
        }
        
        stage('Deploy') {
            steps {
                // Deploy the application (replace with your deployment command)
                sh 'make deploy'
            }
        }
    }
}
