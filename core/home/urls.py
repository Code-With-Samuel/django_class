from django.urls import path
from .views import *

urlpatterns = [
    path('',view_1, name="view_1"),
    path('source/',view_2, name="view_2"),
]