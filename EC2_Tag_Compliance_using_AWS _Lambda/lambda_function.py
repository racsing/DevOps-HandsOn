import json
from datetime import datetime
from dateutil.relativedelta import relativedelta
import boto3
import email_service


def lambda_handler(event, context):
    ec2_resource = boto3.resource('ec2')

    # filter all running instances
    filters = [{'Name': 'instance-state-name', 'Values': ['running']}]

    # Declared dictionary to store running instances
    instances = ec2_resource.instances.filter(Filters=filters)

    required_keys = ['Name', 'Environment']

    # looping through all the running instance
    for instance in instances:
        existing_keys = []
        missing_keys = []
        schedule_terminate = None
        recipient = ''

        # Fetching tags for each instance
        for tags in instance.tags:
            if tags['Key'] in required_keys:
                existing_keys.append(tags['Key'])

            if tags['Key'] == 'Terminate':
                schedule_terminate = tags['Value']

            if tags['Key'] == 'CreatedBy':
                recipient = tags['Value']

        # Finding missing keys for each instance
        for key in required_keys:
            if key not in existing_keys:
                missing_keys.append(key)

        # Check for missing keys, if any
        if missing_keys is not []:
            # Store current date and time
            now = datetime.now()

            # Check if 'Terminate' tag exists
            if schedule_terminate is not None:
                # Check schedule_terminate for instance with missing tags has come or not?
                if schedule_terminate >= str(now):

                    # terminate instance
                    ec2_resource.instances.filter(InstanceIds=[instance.id]).terminate()
                    print("terminated" + str(instance.id))

                    # send email
                    subject = "CRITICAL!! Terminated EC2 Instance"
                    body = ("The EC2 instance with instance-id :" + str(instance.id) +
                            " is missing tags: " + str(missing_keys) + ", Hence got terminated.")
                    response = email_service.send_email(subject, body, recipient)
                    print(response)

                else:

                    # Print time left for the schedule_terminate of ec2 instance
                    terminate_on = datetime.strptime(schedule_terminate, "%d/%m/%Y %H:%M:%S")
                    time_left = (terminate_on - now)
                    print("The EC2 instance with instance-id :" + str(instance.id) +
                          " will be removed in " + str(time_left) + " hours")

            else:
                # Time to terminate EC2 Instance with missing tags
                time_to_terminate = now + relativedelta(hours=6)

                # create the tag
                tags = [{'Key': 'Terminate',
                         'Value': time_to_terminate.strftime("%d/%m/%Y %H:%M:%S")
                         }]
                ec2_resource.create_tags(Resources=[instance.id], Tags=tags)

                # Send an email
                subject = "WARNING!! Missing Tags for EC2 Instance"
                body = ("The EC2 instance with instance-id :" + str(instance.id) +
                        " is missing values: " + str(missing_keys) +
                        ", properly tag the instance to avoid being terminated in 6 hours.")
                response = email_service.send_email(subject, body, recipient)
                print(response)

        else:
            print("The EC2 instance with instance-id :" + str(instance.id) +
                  "has all the required tags.")

    return {
        'statusCode': 200,
        'body': json.dumps('Ok!')
    }
