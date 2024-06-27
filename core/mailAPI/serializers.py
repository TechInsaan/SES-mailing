from rest_framework import serializers


class RegistrationSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    mail_id = serializers.EmailField()


class ForgotPassSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    mail_id = serializers.EmailField()
    otp = serializers.CharField(max_length=100)


class EventRegSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    mail_id = serializers.EmailField()
    event_name = serializers.CharField(max_length=100)
    ticket_id = serializers.CharField(max_length=100)


class SlotBookSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    mail_id = serializers.EmailField()
    event_name = serializers.CharField(max_length=100)
    slot_date = serializers.CharField(max_length=100)
    slot_time = serializers.CharField(max_length=100)

class RejectionSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    mail_id = serializers.EmailField()
    transaction_id = serializers.CharField(max_length=100)

class EventwiseSerializer(serializers.Serializer):
    event_name = serializers.CharField(max_length=100)
    email_array = serializers.ListField(child=serializers.EmailField())
    subject = serializers.CharField(max_length=100)
    htmlPart = serializers.CharField()

class EmailListSerializer(serializers.Serializer):
    email_array = serializers.ListField(child=serializers.EmailField())
    subject = serializers.CharField(max_length=100)
    htmlPart = serializers.CharField()