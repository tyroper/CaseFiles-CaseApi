from rest_framework import serializers
from case.models import Ban, Case, Moderator, Vote


class ModeratorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Moderator
        fields = ('id', 'case', 'userId')


class BanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ban
        fields = ('id', 'case', 'userId', 'moderator', 'banDate')


class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields = ('id', 'case', 'userId', 'upvote')


class CaseVoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields = ('upvote',)


class CaseBanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ban
        fields = ('userId', 'moderator', 'banDate')


class CaseModeratorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Moderator
        fields = ('userId',)


class CaseSerializer(serializers.ModelSerializer):
    caseModerators = CaseModeratorSerializer(many=True, read_only=True)
    caseBans = CaseBanSerializer(many=True, read_only=True)

    votes = serializers.SerializerMethodField()

    def get_votes(self, case):
        upvotes = case.caseVotes.all().filter(upvote=True).count()
        downvotes = case.caseVotes.all().filter(upvote=False).count()
        return upvotes - downvotes

    class Meta:
        model = Case
        fields = ('id', 'userId', 'name', 'crime', 'description',
                  'agency', 'city', 'state', 'county', 'createdDate', 'caseModerators', 'caseBans', 'votes')
