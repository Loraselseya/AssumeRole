import boto3
import datetime

ec2 = boto3.resource('ec2')

date_filter = (datetime.datetime.now() - datetime.timedelta(days=10)).strftime("2023-02-10")

instances = ec2.instances.filter(
    Filters=[{'Name': 'launch-time', 'Values': [date_filter+'*']}])

for instance in instances:
    print(instance.id)

for status in ec2.meta.client.describe_instance_status()['InstanceStatuses']:
    print(status)