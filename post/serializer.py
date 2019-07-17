from .models import Post
from rest_framework import serializers

# serializers의 Serializers는 Django의 Form과 유사한 역할을 한다

# serializer의 ModelSerializer는 Django의 ModelForm과 유사한 역할을 한다

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        #fields = ['title', 'body']
        fields = '__all__'
