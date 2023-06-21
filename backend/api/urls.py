from django.urls import path, include
from rest_framework.routers import SimpleRouter

from .views import NewsViewSet, CommentsViewSet


app_name = 'api'

router = SimpleRouter()

router.register('news', NewsViewSet)
router.register(
    r'news/(?P<news_id>\d+)/comments',
    CommentsViewSet,
    basename='comments'
)

urlpatterns = [
    path('', include(router.urls)),
]
