from django.urls import path
from .views import ChallengeListView, serve_challenges,solve_challenge

urlpatterns = [

    path('', serve_challenges, name='challenges'),
    path('api/', ChallengeListView.as_view(), name='challenge-list'),
    path('solve/<int:challenge_id>/', solve_challenge, name='solve_challenge'), 
]

