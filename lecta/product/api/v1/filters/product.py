from django_filters import rest_framework as filters

from product.models import Product


class ProductFilter(filters.FilterSet):
    title = filters.CharFilter(lookup_expr="icontains")

    class Meta:
        model = Product
        fields = ("title",)
