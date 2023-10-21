from django.urls import path
from . import views

urlpatterns = [
    path('button/',views.button),
    path('send_email/',views.send_email),
]