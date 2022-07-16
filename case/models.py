from django.db import models
from django.utils import timezone


class Case(models.Model):
    userId = models.BigIntegerField(null=False)
    name = models.CharField(max_length=255, null=False)
    crime = models.CharField(max_length=255, null=False)
    description = models.TextField(null=False)
    agency = models.CharField(max_length=255, null=False)
    city = models.CharField(max_length=255, null=False)
    state = models.CharField(max_length=255, null=False)
    county = models.CharField(max_length=255, null=False)
    createdDate = models.DateTimeField(default=timezone.now, null=False)
    solveDate = models.DateTimeField(null=True)

    class Meta:
        ordering = ('-createdDate',)

    def __str__(self):
        return self.name


class Moderator(models.Model):
    case = models.ForeignKey(
        Case, on_delete=models.CASCADE, related_name='caseModerators')
    userId = models.BigIntegerField(null=False)


class Ban(models.Model):
    case = models.ForeignKey(
        Case, on_delete=models.CASCADE, related_name='caseBans')
    userId = models.BigIntegerField(null=False)
    moderator = models.ForeignKey(
        Moderator, on_delete=models.CASCADE, related_name='moderatorbans')
    banDate = models.DateTimeField(default=timezone.now, null=False)


class Vote(models.Model):
    case = models.ForeignKey(
        Case, on_delete=models.CASCADE, related_name='caseVotes')
    userId = models.BigIntegerField(null=False)
    upvote = models.BooleanField(null=False, default=False)
