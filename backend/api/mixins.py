from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.mixins import (
    CreateModelMixin, UpdateModelMixin, ListModelMixin, DestroyModelMixin
)


class CreateListDestroyViewSet(
    CreateModelMixin,
    ListModelMixin,
    DestroyModelMixin,
    viewsets.GenericViewSet
):
    pass
