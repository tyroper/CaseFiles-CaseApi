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
    class ModeratorObjects(models.Manager):
        def get_queryset(self, caseId):
            return super().get_queryset().filter(self.case.Id == caseId)

    case = models.ForeignKey(Case, on_delete=models.CASCADE)
    userId = models.BigIntegerField(null=False)
    objects = models.Manager()
    moderatorobjects = ModeratorObjects()


class Ban(models.Model):
    class BanObjects(models.Manager):
        def get_queryset(self, caseId):
            return super().get_queryset().filter(self.case.Id == caseId)

    case = models.ForeignKey(Case, on_delete=models.CASCADE)
    userId = models.BigIntegerField(null=False)
    moderatorUserId = models.BigIntegerField(null=False)
    banDate = models.DateTimeField(default=timezone.now, null=False)
    objects = models.Manager()
    banobjects = BanObjects()


class Vote(models.Model):
    class VoteObjects(models.Manager):
        def get_queryset(self, caseId):
            return super().get_queryset().filter(self.case.Id == caseId)

    case = models.ForeignKey(Case, on_delete=models.CASCADE)
    userId = models.BigIntegerField(null=False)
    upvote = models.BooleanField(null=False, default=False)
    objects = models.Manager()
    voteobjects = VoteObjects()
