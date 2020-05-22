from django.urls import path, include

# from product_detail.view import *
from .views import *

app_name='renderer'

urlpatterns = [
     path('', MyView.as_view())
]