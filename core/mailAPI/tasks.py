#https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ses.html
from celery import shared_task
from django.conf import settings
import boto3
import json

@shared_task
def send_reg_mail(mail_id, name):
    # sts_client = boto3.client('sts')
    # assumed_role_object=sts_client.assume_role(
    #     RoleArn="arn:aws:iam::account-of-role-to-assume:role/name-of-role",
    #     RoleSessionName="AssumeRoleSession1"
    # )
    # credentials=assumed_role_object['Credentials']
    ses = boto3.client(
        'ses',
        aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
        aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
        region_name='ap-south-1',
        # aws_session_token=credentials['SessionToken']
    )
    data = {
        'name': name,
    }
    response = ses.send_templated_email(
        Source=' "PICT ACM Student Chapter" <noreply@pulzion.co.in>',
        Destination={
            'ToAddresses': [
                mail_id,
            ]
        },
        Template='register',
        TemplateData=json.dumps(data),
    )

    print(response)
    return response


@shared_task
def send_forgot_password_mail(mail_id, name, otp):
    ses = boto3.client(
        'ses',
        aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
        aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
        region_name='ap-south-1',
        # aws_session_token=settings.AWS_SESSION_TOKEN
    )
    data = {
        'name': name,
        'otp': otp,
    }
    response = ses.send_templated_email(
        Source=' "PICT ACM Student Chapter" <noreply@pulzion.co.in>',
        Destination={
            'ToAddresses': [
                mail_id,
            ]
        },
        Template='Alumni_forgot',
        TemplateData=json.dumps(data)
    )

    print(response)
    return response


@shared_task
def send_event_reg_mail(mail_id, name, event_name, ticket_id):
    ses = boto3.client(
        'ses',
        aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
        aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
        region_name='ap-south-1',
        # aws_session_token=settings.AWS_SESSION_TOKEN
    )
    data = {
        'name': name,
        'event_name': event_name,
        'ticket_id': ticket_id,
    }
    response = ses.send_templated_email(
        Source=' "PICT ACM Student Chapter" <noreply@pulzion.co.in>',
        Destination={
            'ToAddresses': [
                mail_id,
            ]
        },
        Template='event',
        TemplateData=json.dumps(data)
    )

    print(response)
    return response


@shared_task
def send_slot_book_mail(mail_id, name, event_name, slot_date, slot_time):
    ses = boto3.client(
        'ses',
        aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
        aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
        region_name='ap-south-1',
        # aws_session_token=settings.AWS_SESSION_TOKEN
    )
    data = {
        'name': name,
        'event_name': event_name,
        'slot_date': slot_date,
        'slot_time': slot_time
    }
    response = ses.send_templated_email(
        Source=' "PICT ACM Student Chapter" <noreply@pulzion.co.in>',
        Destination={
            'ToAddresses': [
                mail_id,
            ]
        },
        Template="slot",
        TemplateData=json.dumps(data)
    )

    print(response)
    return response

@shared_task
def send_reject_mail(mail_id, name, transaction_id):
    # sts_client = boto3.client('sts')
    # assumed_role_object=sts_client.assume_role(
    #     RoleArn="arn:aws:iam::account-of-role-to-assume:role/name-of-role",
    #     RoleSessionName="AssumeRoleSession1"
    # )
    # credentials=assumed_role_object['Credentials']
    ses = boto3.client(
        'ses',
        aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
        aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
        region_name='ap-south-1',
        # aws_session_token=credentials['SessionToken']
    )
    data = {
        'name': name,
        'transaction_id': transaction_id
    }
    response = ses.send_templated_email(
        Source=' "PICT ACM Student Chapter" <noreply@pulzion.co.in>',
        Destination={
            'ToAddresses': [
                mail_id,
            ]
        },
        Template='reject',
        TemplateData=json.dumps(data),
    )

    print(response)
    return response

@shared_task
def eventwiseMessage(event_name, subject, htmlPart, email_array):
    ses = boto3.client(
        'ses',
        aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
        aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
        region_name='ap-south-1',
        # aws_session_token=settings.AWS_SESSION_TOKEN
    )
    data = {
        'event_name': event_name,
    }
    response = ses.send_email(
        Destination={
            'ToAddresses': email_array,
        },
        Message={
            'Body': {
                'Html': {
                    'Charset': 'UTF-8',
                    'Data': htmlPart,
                },
            },
            'Subject': {
                'Charset': 'UTF-8',
                'Data': subject,
            },
        },
        Source=' "PICT ACM Student Chapter" <noreply@pulzion.co.in>',
    )

    print(response)
    return response

@shared_task
def sendMailToList(subject, htmlPart, email_array):
    ses = boto3.client(
        'ses',
        aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
        aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
        region_name='ap-south-1',
        # aws_session_token=settings.AWS_SESSION_TOKEN
    )
    breakFlag = False
    for i in range(0, len(email_array), 45):
        if((i + 45) > len(email_array)):
            last_index = len(email_array)
            breakFlag = True
        else:
            last_index = i + 45
        emailList = email_array[i:last_index]
        print(emailList)
        response = ses.send_email(
            Destination={
                'ToAddresses': emailList,
            },
            Message={
                'Body': {
                    'Html': {
                        'Charset': 'UTF-8',
                        'Data': htmlPart,
                    },
                },
                'Subject': {
                    'Charset': 'UTF-8',
                    'Data': subject,
                },
            },
            Source=' "PICT ACM Student Chapter" <noreply@pulzion.co.in>',
        )
        if(breakFlag):
            print('break true')
            break 

    print(response)
    return response