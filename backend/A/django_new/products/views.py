from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Product
from .serializers import ProductSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

class ProductViewSet(viewsets.ModelViewSet):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer

@api_view(['POST'])
def product_list(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    message = "succsess"
    return Response({'message': message}, status=status.HTTP_200_OK)

@api_view(['GET'])
def get_product_list(request):

    if request.method == 'GET':
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)