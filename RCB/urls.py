from django.urls import path
from RCB.views import  *
app_name='nothing'
urlpatterns=[
    path('Kruthi/',Kruthi,name='Kruthi'),
    path('Akshaya/',Akshaya,name='Akshaya'),
]
