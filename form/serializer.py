from rest_framework import serializers

from create.models import testdata


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model= testdata
        fields = ("field_name", "type","options","mandatory")