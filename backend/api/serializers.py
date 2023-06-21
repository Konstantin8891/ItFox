from rest_framework import serializers

from posts.models import News, Comments
from users.models import Users


class CommentsCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comments
        fields = ('text', 'author_id', 'post_id')


class CommentsViewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comments
        fields = ('id', 'text', 'author_id')


class NewsCreateSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(queryset=Users.objects.all())

    class Meta:
        model = News
        fields = ('id', 'title', 'text', 'author', 'likes')


class NewsViewSerializer(serializers.ModelSerializer):
    comments = serializers.SerializerMethodField()

    class Meta:
        model = News
        fields = ('id', 'title', 'text', 'author', 'likes', 'comments')

    def get_comments(self, obj):
        comments = obj.comments.all()
        if len(comments) > 10:
            comments = comments[-10:]
        return CommentsViewSerializer(comments, many=True).data
