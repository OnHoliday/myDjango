from django.urls import path, include
from registrationapp import views

app_name = 'registrationapp'

urlpatterns=[
    path('register/', views.register, name="register"),
    path('user_login/', views.user_login, name='user_login'),
]
