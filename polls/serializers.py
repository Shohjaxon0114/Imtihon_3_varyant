from rest_framework import serializers
from .models import YangilikModels

class YangilikSerializer(serializers.ModelSerializer):
    Y_nomi = serializers.CharField()
    Y_turi = serializers.CharField()
    Y_matni = serializers.CharField()
    Y_vaxti = serializers.DateField()


    class Meta:
        model = YangilikModels
        fields = ('Y_nomi','Y_turi','Y_matni','Y_vaxti','Y_vaxti')
