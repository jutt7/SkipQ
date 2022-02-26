-Website Monitering
    This project measures the availabilty and latency of provided websites on interval of 1 minutes and send notfication (SNS) via Email 
    to cercing person whenever availabilty drops below threshold point or latency exceeds the threshold point. The project also save the
    important information from notfication to a table in DynamoDB.
    
    To run the project you have to setup the virtual environment on Clound9 amazon console. Steps required to setup the environment
    are given below:
    1- create account on https://signin.aws.amazon.com/
    2- Search for Cloud9 in the search dialog.
    3-Press on Create Environment button in top right corner and enter a Name and Short description for the environment.
    4-Select Create a new EC2 instance for environment (direct access) from Environment type.
    5-Select t2.micro (1 GiB RAM + 1 vCPU) from Instance type.
    6-Select Ubuntu Server 18.04 LTS from Platform.
    7-Select proper cost saving setting and click on next step button and your environment will be created in a few minutes.
    
    Open the created virtual and clone the the project with following command
    git clone https://github.com/MuhammadAwais2021skipq/ProximaCentauri.git
    Once cloned; go to project directory and install all the packages given in Requirements.txt file.
    Run the project with cdk synth command and deploy it on amazon console with cdk deploy command.
    
    You can now check latency and availabilty on amazon console. 
    