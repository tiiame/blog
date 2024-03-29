from rest_framework.serializers import ModelSerializer
from common.models import *
from django.contrib.auth.models import User

class SkillSerializer(ModelSerializer):

    class Meta:
        model = Skill
        fields = "__all__"

    
from rest_framework import serializers


class SkilSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=200)
    percentage = serializers.IntegerField()
    order = serializers.IntegerField()

    def create(self, validated_data):
        title = validated_data.get('title')
        percentage = validated_data.get('percentage')
        order = validated_data.get('order')
        isinstance = Skill.objects.create(
            title=title,
            percentage=percentage,
            order=order
        )   
        

class ProfileSerializer(serializers.Serializer):
    full_name = serializers.CharField(max_length=200)
    image = serializers.ImageField()
    bio = serializers.CharField()

class BlogCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Blog
        fields = ('title', 'description', 'category')
 
class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name','last_name', 'username' )



class BlogListSerializer(serializers.ModelSerializer):
    category = serializers.CharField(source='category.name')
    author = AuthorSerializer

    class Meta:
        model = Blog
        fields = "__all__"

class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = "__all__"

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = "__all__"


class PortfolioSerializer(serializers.ModelSerializer):

    class Meta:
        model = Portfolio
        fields = "__all__"



