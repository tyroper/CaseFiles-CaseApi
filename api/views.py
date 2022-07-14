from rest_framework import generics
from case.models import Ban, Case, Moderator, Vote
from .serializers import CaseSerializer


class CaseList(generics.ListCreateAPIView):
    queryset = Case.objects.all()
    serializer_class = CaseSerializer
    pass


class CaseDetail(generics.RetrieveDestroyAPIView):
    queryset = Case.objects.all()
    serializer_class = CaseSerializer
    pass
