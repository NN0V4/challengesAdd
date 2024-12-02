from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Challenges, ChallengesResults
from django.shortcuts import render
from .serializers import ChallengeSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth.models import User

@api_view(['POST'])
def solve_challenge(request, challenge_id):
    user = request.user  
    
    
    try:
        challenge = Challenges.objects.get(id=challenge_id)
    except Challenges.DoesNotExist:
        return Response({"detail": "Challenge not found."}, status=status.HTTP_404_NOT_FOUND)
    
    # Check if the user already solved this challenge
    challenge_result, created = ChallengesResults.objects.get_or_create(user=user, challenge=challenge)
    
    # Update the challenge result
    if not created and challenge_result.solved:
        return Response({"detail": "Challenge already solved."}, status=status.HTTP_400_BAD_REQUEST)
    
    challenge_result.solved = True  # Mark as solved
    challenge_result.points_earned = challenge.points  # Assign points
    challenge_result.save()
    
    return Response({"detail": "Challenge solved successfully!"}, status=status.HTTP_200_OK)




def serve_challenges(request):
    return render(request, 'challenges/index.html')


class ChallengeListView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        challenges = Challenges.objects.all()
        serializer = ChallengeSerializer(challenges, many=True,context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)
