from rest_framework import serializers
from api.models import Role

class PagerSerializers(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = "__all__"