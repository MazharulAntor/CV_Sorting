from datetime import datetime

from django.db import models


class Skill(models.Model):
    skill_name = models.CharField(max_length=50)
    score = models.FloatField(default=0)


class TopCandidates(models.Model):
    number_of_selection = models.IntegerField()
    date = models.DateTimeField(default=datetime.now, blank=True)

