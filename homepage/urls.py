from django.urls import path
from .views import home

urlpatterns = [
    path('', home, name='home'),  
    path('api/home/', home, name='homepage_data'),
]

