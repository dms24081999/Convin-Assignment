from ..models import FileModel
from rest_framework import serializers

class FileModelSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    document_hash= serializers.CharField(required=False)
    email = serializers.CharField(required=True)
    phone = serializers.CharField(required=True)
    

    class Meta:
        model = FileModel
        fields= ('id','email','document','document_hash','phone')

