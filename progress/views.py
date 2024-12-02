from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from challenges.models import Categories, Challenges, ChallengesResults, Hints
from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.db.models import Sum, Count,Q
from django.db.models import Q


class UserProgressView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        
        
        solved_results = ChallengesResults.objects.filter(user=user, solved=True)
        total_points_earned = solved_results.aggregate(Sum('points_earned'))['points_earned__sum'] or 0
        challenges_solved_count = solved_results.count()

    
        total_challenges = Challenges.objects.count()
        total_points = Challenges.objects.aggregate(Sum('points'))['points__sum'] or 0

        
        category_stats = Categories.objects.annotate(
            total_challenges=Count('challenges'),
            solved_challenges=Count('challenges', filter=Q(challenges__challengesresults__user=user, challenges__challengesresults__solved=True)),
            points_earned=Sum('challenges__challengesresults__points_earned', filter=Q(challenges__challengesresults__user=user))
        ).values('name', 'total_challenges', 'solved_challenges', 'points_earned')

        return Response({
            "total_challenges": total_challenges,
            "challenges_solved_count": challenges_solved_count,
            "total_points": total_points,
            "points_earned": total_points_earned,
            "category_stats": list(category_stats)
        }, status=status.HTTP_200_OK)
