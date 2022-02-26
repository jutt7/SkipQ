
# -WebHealth Monitering
   **This project measures the availabilty and latency of provided websites on interval of 1 minutes.**
    
   **To run the project you have to setup the virtual environment on Clound9 amazon console. Steps required to setup the environment**
    **are given below:**
    
    
     1- create account on https://signin.aws.amazon.com/
     2- Search for Cloud9 in the search dialog.
     3-Press on Create Environment button in top right corner and enter a Name and Short description for the environment.
     4-Select Create a new EC2 instance for environment (direct access) from Environment type.
     5-Select t2.micro (1 GiB RAM + 1 vCPU) from Instance type.
     6-Select Ubuntu Server 18.04 LTS from Platform.
     7-Select proper cost saving setting and click on next step button and your environment will be created in a few minutes.
     
    
   **Now check the current version of python and if it is not pytho3 go to bashrc file**
   > vim ~/.bashrc
   
   **and add following line and save the file**
   
   > alias python=/usr/bin/python3
   
   **now update the aws cli with followin commands:**
   
    
      curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
      unzip awscliv2.zip
      sudo ./aws/install
    
    
   **Now make a folder to install the project with following command**
    
   > mkdir folderName
    
  **change current directory to newly created folder**
    
   > cd folderName
    
   **Now create a new cdk project**
    
  >  cdk init app --language python
    
   **Go to virtual environment with followin command:**
   > source .venv/bin/activate
    
   **Now install the following packages:**
   
    
    python -m pip install aws-cdk.core==1.135.0
    python -m pip install -r requirements.txt
    nvm install v16.3.0 && nvm use v16.3.0 && nvm alias default v16.3.0
    npm install -g aws-cdk
    export PATH=$PATH:$(npm get prefix)/bin
    .venv/bin/pip3.6 install -r requirements.txt
    
    
   **After writing code for availabilty and latency synth and deploy the project on AWS Lambda with following command:**
   > cdk synth
   > cdk deploy
    
    
  **You can now check latency and availabilty on amazon console.**
    
