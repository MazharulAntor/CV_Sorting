from django.db import models


class Skill(models.Model):
    skill_name = models.CharField(max_length=50)
    score = models.FloatField(default=0)
