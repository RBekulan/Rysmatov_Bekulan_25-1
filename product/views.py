from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serlializers import *


@api_view(['GET'])
def test(request):
    dict_ = {
        'text': "hello world",
    }
    return Response(data=dict_)


@api_view(['GET'])
def product_list_api_view(request):
    products = Products.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(data=serializer.data)


@api_view(['GET'])
def product_detail_api_view(request, id):
    try:
        products = Products.objects.get(id=id)
    except Products.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = ProductSerializer(products)
    return Response(data=serializer.data)


@api_view(['GET'])
def categories_list_api_view(request):
    category = Category.objects.all()
    serializer = CategorySerializer(category, many=True)
    return Response(data=serializer.data)


@api_view(['GET'])
def categories_detail_api_view(request, id):
    try:
        category = Category.objects.get(id=id)
    except Category.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = CategorySerializer(category)
    return Response(data=serializer.data)


@api_view(['GET'])
def review_list_api_view(request):
    review = Review.objects.all()
    serializer = ReviewSerializer(review, many=True)
    return Response(data=serializer.data)


@api_view(['GET'])
def review_detail_api_view(request, id):
    try:
        review = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = ReviewSerializer(review)
    return Response(data=serializer.data)
