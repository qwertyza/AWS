import json
import boto3

def lambda_handler(event, context):
    client = boto3.client('ecs')
    print("Running task.")
    response = client.run_task(
        cluster='okulagin-fargate-cluster', 
        launchType='FARGATE',
        taskDefinition='fartgate-okulagin:5', 
        count=1,
        networkConfiguration={
            'awsvpcConfiguration': {
                'subnets': ['subnet-103d4d76'],
                'securityGroups': ['sg-07918d3c58e3b9ef8'] ,
                'assignPublicIp': 'ENABLED'
            }
        },
        overrides= {
      'containerOverrides': [
                                {
                                    'name': 'pyinstaller-okulagin',
                                    'environment': [
                                        {
                                            'name': 'INPUT_PYFILE_URL',
                                            'value': 'https://okulaginide.s3-eu-west-1.amazonaws.com/Main.py'
                                        },
                                         {
                                            'name': 'OUTPUT_BUCKET',
                                            'value': 's3://okulaginide'
                                        },
                                    ]
                    
                                },
                             ]
        }
        
            
        )
    print("Finished invoking task.")
