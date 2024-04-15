from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from product.api.v1.filters.product import ProductFilter
from product.api.v1.serializers.product import (
    ProductSerializer,
    ProductFilterSerializer,
)
from product.api.v1.services.product import get_suggestion
from product.models import Product, SearchHistory


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (IsAuthenticated,)

    @action(detail=False, methods=["post"], url_path="search")
    def search_product(self, request):
        serializer = ProductFilterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        filterset = ProductFilter(request.data, queryset=self.get_queryset())
        filterset.is_valid()
        queryset = get_suggestion(filterset.qs, request)
        return Response(queryset)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        SearchHistory.objects.create(
            product_id=instance.id, session_id=request.session.session_key
        )
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
