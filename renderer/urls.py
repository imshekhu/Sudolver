from django.urls import path, include

# from product_detail.view import *
from .views import *

app_name='renderer'

urlpatterns = [
     path('', HomeView.as_view(),  name='homepage'),
     path('new-entry/', OwnBoardView.as_view(), name='new-entry'),
]