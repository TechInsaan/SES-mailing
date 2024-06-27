from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema
from .tasks import * 
from .serializers import *
# Create your views here.


class SendRegMail(APIView):

    @swagger_auto_schema(request_body=RegistrationSerializer)
    def post(self, request):
        serialized = RegistrationSerializer(data=request.data)
        if serialized.is_valid():
            celery_task = send_reg_mail.apply_async(
                kwargs={'name': serialized.data.get('name'), 
                'mail_id': serialized.data.get('mail_id')},
            )

            response_data = {
                'state': celery_task.state,
                'details': serialized.data,
            }
            return Response(response_data)
        
        return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)


class SendForgotPassMail(APIView):

    @swagger_auto_schema(request_body=ForgotPassSerializer)
    def post(self, request):
        serialized = ForgotPassSerializer(data=request.data)
        if serialized.is_valid():
            celery_task = send_forgot_password_mail.apply_async(
                kwargs={'name': serialized.data.get('name'), 
                'mail_id': serialized.data.get('mail_id'), 
                'otp': serialized.data.get('otp')},
            )

            response_data = {
                'state': celery_task.state,
                'details': serialized.data,
            }
            return Response(response_data)
        
        return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)


class SendEventRegMail(APIView):

    @swagger_auto_schema(request_body=EventRegSerializer)
    def post(self, request):
        serialized = EventRegSerializer(data=request.data)
        if serialized.is_valid():
            celery_task = send_event_reg_mail.apply_async(
                kwargs={'name': serialized.data.get('name'), 
                'mail_id': serialized.data.get('mail_id'), 
                'event_name': serialized.data.get('event_name'), 
                'ticket_id': serialized.data.get('ticket_id')},
            )

            response_data = {
                'state': celery_task.state,
                'details': serialized.data,
            }
            return Response(response_data)
        
        return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)
    

class SendSlotBookMail(APIView):

    @swagger_auto_schema(request_body=SlotBookSerializer)
    def post(self, request):
        serialized = SlotBookSerializer(data=request.data)
        if serialized.is_valid():
            celery_task = send_slot_book_mail.apply_async(
                kwargs={'name': serialized.data.get('name'), 
                'mail_id': serialized.data.get('mail_id'), 
                'event_name': serialized.data.get('event_name'), 
                'slot_date': serialized.data.get('slot_date'), 
                'slot_time': serialized.data.get('slot_time')},
            )

            response_data = {
                'state': celery_task.state,
                'details': serialized.data,
            }
            return Response(response_data)
        
        return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)


class SendRejectMail(APIView):

    @swagger_auto_schema(request_body=RejectionSerializer)
    def post(self, request):
        serialized = RejectionSerializer(data=request.data)
        if serialized.is_valid():
            celery_task = send_reject_mail.apply_async(
                kwargs={'name': serialized.data.get('name'), 
                'mail_id': serialized.data.get('mail_id'), 
                'transaction_id': serialized.data.get('transaction_id')}, 
            )

            response_data = {
                'state': celery_task.state,
                'details': serialized.data,
            }
            return Response(response_data)
        
        return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)

class SendEventwiseMail(APIView):

    @swagger_auto_schema(request_body=EventwiseSerializer)
    def post(self, request):
        serialized = EventwiseSerializer(data=request.data)
        if serialized.is_valid():
            celery_task = eventwiseMessage.apply_async(
                kwargs={'event_name': serialized.data.get('event_name'),
                        'email_array': serialized.data.get('email_array'),
                        'subject': serialized.data.get('subject'),
                        'htmlPart': serialized.data.get('htmlPart'), }, 
            )

            response_data = {
                'state': celery_task.state,
                'details': serialized.data,
            }
            return Response(response_data)
        
        return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)

class sendListMail(APIView):

    @swagger_auto_schema(request_body=EmailListSerializer)
    def post(self, request):
        serialized = EmailListSerializer(data=request.data)
        if serialized.is_valid():
            celery_task = sendMailToList.apply_async(
                kwargs={'email_array': serialized.data.get('email_array'),
                        'subject': serialized.data.get('subject'),
                        'htmlPart': serialized.data.get('htmlPart'), }, 
            )

            response_data = {
                'state': celery_task.state,
                'details': serialized.data,
            }
            return Response(response_data)
        
        return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)