from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['name', 'price']
    def create(self, validated_data):
        product = Product.objects.create(**validated_data)
        return product

    def to_representation(self, instance):
        if self.context.get('request').method == 'POST':
            return {'message': 'success'}
        return super().to_representation(instance)