from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
    path('register/', views.SendRegMail.as_view(), name='register'),
    path('forgot/', views.SendForgotPassMail.as_view(), name='forgot_password'),
    path('event/', views.SendEventRegMail.as_view(), name='event_registration'),
    path('slot/', views.SendSlotBookMail.as_view(), name='slot_booking'),
    path('reject/', views.SendRejectMail.as_view(), name='reject'),
    path('eventwise/', views.SendEventwiseMail.as_view(), name='eventwise'),
    path('emaillist/', views.sendListMail.as_view(), name='emaillist'),
]