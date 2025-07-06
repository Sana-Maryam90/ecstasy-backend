from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from ..models import Product
from rest_framework import status
from ..serializers.product_serializers import ProductSerializer

@api_view(['GET'])
def product_list(request):
    category = request.GET.get('category')  # ?category=notebook
    if category:
        products = Product.objects.filter(category__name__iexact=category)
    else:
        products = Product.objects.all()
    
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def product_detail(request, pk):
    try:
        product = Product.objects.get(pk=pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)
    except Product.DoesNotExist:
        return Response({'error': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)