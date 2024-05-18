from .models import Films
from rest_framework import serializers
from authentication.models import User

class FilmsSerializer(serializers.ModelSerializer):
    genre = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Films
        exclude = ['actors', 'direct']

class FilmsDetailSerializer(serializers.ModelSerializer):
    genre = serializers.StringRelatedField(many=True, read_only=True)
    direct = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Films
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    favorite_films = serializers.StringRelatedField(many=True)
    favorite_serials = serializers.StringRelatedField(many=True)
    
    class Meta:
        model = User
        fields = '__all__'
    
    def validate(self,value):
        if (len(value.get('username'))<5):
            raise serializers.ValidationError('Username должен быть больше 5 символов') 

class UserDetailSerializer(serializers.ModelSerializer):
    favorite_films = serializers.StringRelatedField(many=True)
    favorite_serials = serializers.StringRelatedField(many=True, required=False)

    class Meta:
        model = User
        fields = '__all__'