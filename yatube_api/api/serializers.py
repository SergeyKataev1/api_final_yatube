from posts.models import Comment, Follow, Group, Post, User
from rest_framework import serializers
from rest_framework.relations import SlugRelatedField
from rest_framework.serializers import CurrentUserDefault, ModelSerializer
from rest_framework.validators import UniqueTogetherValidator


class CommentSerializer(ModelSerializer):
    '''Серилизатор комментариев.'''
    author = SlugRelatedField(
        read_only=True, slug_field='username'
    )

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ['post']


class FollowSerializer(ModelSerializer):
    '''Серилизатор подписок.'''
    user = SlugRelatedField(
        read_only=True,
        slug_field='username',
        default=CurrentUserDefault()
    )
    following = SlugRelatedField(
        slug_field='username',
        queryset=User.objects.all()
    )

    class Meta:
        model = Follow
        fields = '__all__'
        validators = [UniqueTogetherValidator(
            queryset=Follow.objects.all(),
            fields=['user', 'following'])]

    def validate(self, data):
        if self.context['request'].user != data.get('following'):
            return data
        raise serializers.ValidationError(
            'Подписка на себя запрещена'
        )


class GroupSerializer(ModelSerializer):

    class Meta:
        model = Group
        fields = '__all__'


class PostSerializer(ModelSerializer):
    '''Серилизатор постов.'''
    author = SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        model = Post
        fields = '__all__'
