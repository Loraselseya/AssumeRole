import boto3
import datetime

ec2 = boto3.resource('ec2')

date_filter = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime("2023-02-10")

instances = ec2.instances.filter(
    Filters=[{'Name': 'launch-time', 'Values': [date_filter+'*']}])

for instance in instances:
    print(instance.id)

