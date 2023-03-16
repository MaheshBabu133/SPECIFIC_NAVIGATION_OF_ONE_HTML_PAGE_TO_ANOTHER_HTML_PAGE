from django.urls import path
from CSK.views import *
app_name='something'
urlpatterns=[
    path('teju/',teju,name='teju'),
    path('nithya/',nithya,name='nithya'),
]
