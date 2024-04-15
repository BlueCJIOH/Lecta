from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from category.models import Category
from category.api.v1.serializers.category import CategorySerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
