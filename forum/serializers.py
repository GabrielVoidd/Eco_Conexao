from rest_framework import serializers
from .models import Post, Comment, Topic, SubTopic
from django.contrib.auth.models import User


class TopicSerializer(serializers.ModelSerializer):
    #author = serializers.SerializerMethodField()

    class Meta:
        model = Topic
        fields = '__all__'

        #def get_author(self, obj):
            #return obj.author.username


class SubTopicSerializer(serializers.ModelSerializer):
    #title = serializers.SerializerMethodField()

    class Meta:
        model = SubTopic
        fields = '__all__'

        #def get_title(self, obj):
            #return obj.title.title


class PostSerializer(serializers.ModelSerializer):
    like_count = serializers.IntegerField(source='likes.count', read_only=True)

    author = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'author', 'subtopic', 'created_at', 'like_count']

    def get_author(self, obj):
        return obj.author.username


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = '__all__'

    def get_author(self, obj):
        return obj.author.username


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password']
        )
        return user
