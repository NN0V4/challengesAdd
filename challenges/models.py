from django.db import models
from django.contrib.auth.models import User


class Categories(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name  


class Challenges(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    link = models.CharField(max_length=255, blank=True, null=True)
    timer = models.IntegerField()  
    flag = models.CharField(max_length=255)
    level = models.CharField(max_length=10, blank=True, null=True)  
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)  
    nc=models.CharField(max_length=255,blank=True, null=True)
    points = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.title  


class ChallengesResults(models.Model):  
    user = models.ForeignKey(User, on_delete=models.CASCADE)  
    challenge = models.ForeignKey(Challenges, on_delete=models.CASCADE)
    solved = models.BooleanField(blank=True, null=True)
    points_earned = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f"{self.user.username} - {self.challenge.title}"


class Hints(models.Model):
    challenge = models.ForeignKey(Challenges, on_delete=models.CASCADE,related_name='hints')  
    hint_text = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.hint_text
