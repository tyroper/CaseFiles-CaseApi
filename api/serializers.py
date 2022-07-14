from rest_framework import serializers
from case.models import Case


class CaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Case
        fields = ('userId', 'name', 'crime', 'description',
                  'agency', 'city', 'state', 'county', 'createdDate')
