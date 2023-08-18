from rest_framework import serializers
from .models import YangilikModels

class YangilikSerializer(serializers.ModelSerializer):



    class Meta:
        model = YangilikModels
        fields = ('Y_nomi','Y_turi','Y_matni','Y_vaxti','Y_vaxti','user')
