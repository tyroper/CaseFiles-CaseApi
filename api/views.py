from rest_framework import generics
from case.models import Ban, Case, Moderator, Vote
from .serializers import BanSerializer, CaseSerializer, ModeratorSerializer, VoteSerializer


class CaseList(generics.ListCreateAPIView):
    queryset = Case.objects.all()
    serializer_class = CaseSerializer
    pass


class CaseDetail(generics.RetrieveDestroyAPIView):
    queryset = Case.objects.all().prefetch_related(
        'caseBans', 'caseModerators', 'caseVotes')
    serializer_class = CaseSerializer
    pass


class BanList(generics.ListCreateAPIView):
    queryset = Ban.objects.all()
    serializer_class = BanSerializer
    pass


class BanDetail(generics.RetrieveDestroyAPIView):
    queryset = Ban.objects.all()
    serializer_class = BanSerializer
    pass


class ModeratorList(generics.ListCreateAPIView):
    queryset = Moderator.objects.all()
    serializer_class = ModeratorSerializer
    pass


class ModeratorDetail(generics.RetrieveDestroyAPIView):
    queryset = Moderator.objects.all()
    serializer_class = ModeratorSerializer
    pass


class VoteList(generics.ListCreateAPIView):
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer
    pass


class VoteDetail(generics.RetrieveDestroyAPIView):
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer
    pass
