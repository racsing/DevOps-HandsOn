from botocore.exceptions import ClientError
import boto3


# Method to send email
def send_email(subject, body, recipient):
    sender = "rachanas.work@gmail.com"
    charset = "UTF-8"
    ses_client = boto3.client('ses')

    try:
        response = ses_client.send_email(
            Destination={
                'ToAddresses': [
                    recipient,
                ],
            },
            Message={
                'Body': {
                    'Html': {
                        'Charset': charset,
                        'Data': body,
                    }, },
                'Subject': {
                    'Charset': charset,
                    'Data': subject,
                }, },
            Source=sender,
        )

    except ClientError as err:
        return err.response['Error']['Message']
    else:
        return "Email sent! Message ID:" + str(response['MessageId'])
