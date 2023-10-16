from rest_framework import routers,serializers,viewsets
from .models import Member

class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ['lastname','firstname','phone', 'email','joined_date']


