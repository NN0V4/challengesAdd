from django.urls import path
from .views import UserProgressView

urlpatterns = [
       path('api/', UserProgressView.as_view(), name='user_progress'),
]

