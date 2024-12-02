from django.contrib import admin
from .models import Categories, Challenges, ChallengesResults, Hints

admin.site.register(Categories)
admin.site.register(Challenges)
admin.site.register(ChallengesResults)
admin.site.register(Hints)
