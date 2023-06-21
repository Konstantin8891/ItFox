from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from .mixins import CreateListDestroyViewSet
from .serializers import (
    NewsViewSerializer,
    NewsCreateSerializer,
    CommentsCreateSerializer,
    CommentsViewSerializer
)
from posts.models import News, Comments
from users.models import Users


class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all().order_by('id')
    http_method_names = ['post', 'put', 'delete', 'get']

    def get_serializer_class(self):
        if self.action in ('list', 'retrieve'):
            return NewsViewSerializer
        return NewsCreateSerializer

    def create(self, request, *args, **kwargs):
        if request.user.is_anonymous:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        data = request.data
        user = Users.objects.get(username=request.user)
        data.update({'author': user.id})
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )

    def update(self, request, pk, *args, **kwargs):
        if request.user.is_anonymous:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        data = request.data
        try:
            user = Users.objects.get(username=request.user)
        except Exception:
            Response('User not found', status=status.HTTP_401_UNAUTHORIZED)
        data.update({'author': user.id})
        try:
            news = News.objects.get(id=pk)
        except Exception:
            return Response(
                'News not found', status=status.HTTP_400_BAD_REQUEST
            )
        if user.id != news.author and user.role != 'admin':
            return Response(
                "You don't have right's to edit news",
                status=status.HTTP_403_FORBIDDEN
            )
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data, status=status.HTTP_200_OK)

    def destroy(self, request, *args, **kwargs):
        if request.user.is_anonymous:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        return super().destroy(request)

    @action(detail=True, methods=['GET'])
    def like(self, request, pk, *args, **kwargs):
        news = News.objects.get(id=pk)
        news.likes += 1
        news.save()
        serializer = self.get_serializer(news)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CommentsViewSet(CreateListDestroyViewSet):
    queryset = Comments.objects.all().order_by('id')
    serializer_class = CommentsViewSerializer

    def create(self, request, news_id, *args, **kwargs):
        if request.user.is_anonymous:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        data = request.data
        data.update({'post_id': news_id})

        user = Users.objects.get(username=request.user)
        data.update({'author_id': user.id})
        serializer = CommentsCreateSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        serializer = CommentsViewSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        return Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )

    def destroy(self, request, news_id, pk, *args, **kwargs):
        if request.user.is_anonymous:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        user = Users.objects.get(username=request.user)
        try:
            comment = Comments.objects.get(id=pk)
        except Exception:
            return Response(
                data='Comment not found', status=status.HTTP_400_BAD_REQUEST
            )
        if comment.author_id != user.id and user.role != 'admin':
            return Response(
                data="You don't have rights to delete this comment"
            )
        return super().destroy(request, news_id, pk)
