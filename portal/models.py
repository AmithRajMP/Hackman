from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm


class Team(models.Model):
    team_name = models.CharField(max_length=100, unique=True)
    idea_title = models.CharField(max_length=100)
    idea_description = models.CharField(max_length=1000)

    def __unicode__(self):
        return self.team_name


class Participant(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    college = models.CharField(max_length=100)
    contact = models.CharField(max_length=13)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    is_approved = models.BooleanField()
    is_paid = models.BooleanField()

    def __unicode__(self):
        return self.user.username


class TeamForm(ModelForm):
    class Meta:
        model = Team
        fields = ['team_name', 'idea_title', 'idea_description']
