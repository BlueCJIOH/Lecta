from rest_framework import serializers

from product.models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class ProductFilterSerializer(serializers.Serializer):
    title = serializers.CharField(allow_blank=True)


class ProductSuggestionSerializer(serializers.Serializer):
    title = serializers.CharField()
    price = serializers.DecimalField(max_digits=6, decimal_places=2)
