from django.db import models
from django.conf import settings
from challenges.models import Challenge

from django.contrib.auth.models import User

class Team(models.Model):
    """
    Team model class.
    TODO: Add unique constraints to ensure double adding does not take place
    TODO: Create custom save method to update a field time when points change. 
          that way in case of a tie we can query this feild to see who got there first.
    """

    def _points(self):
        return sum([solve.challenge.points for solve in SolvedChallenge.objects.filter(team__name=self.name)])
    
    def _correct(self):
        return self.solved.all().count()

    name = models.CharField(max_length=150, unique=True)
    email = models.CharField(max_length=50)
    affiliation = models.CharField(max_length=50)

    points = property(_points)
    hidden = models.BooleanField(default=False)
    correct_flags = property(_correct)
    wrong_flags = models.IntegerField(default=0)
    
    created = models.DateTimeField(auto_now_add=True)

    accesscode = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class SolvedChallenge(models.Model):
    """
    Team solved challenge model
    """
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='solved')

    user = models.ForeignKey(User, default=None, null=True, on_delete=models.CASCADE)
    challenge = models.ForeignKey(Challenge, default=None, null=True, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
