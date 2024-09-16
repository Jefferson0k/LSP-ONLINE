from rest_framework import serializers
from .models import Palabras

class PalabrasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Palabras
        fields = ('id','title','description','done','created_at')
        read_only_fields =('id','created_at')