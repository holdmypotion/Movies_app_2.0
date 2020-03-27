from django.urls import path

from login import views


app_name = 'login'

urlpatterns = [
    path('', views.signup_page, name='signup_page'),
]
