from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from .serlializers import *
from .models import *


class CategoryListAPIView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return CategorySerializer
        return self.serializer_class


class CategoryDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get_serializer_class(self):
        if self.request.method == 'PUT':
            return CategorySerializer
        return self.serializer_class


class ProductsListAPIView(ListCreateAPIView):
    queryset = Products.objects.all()
    serializer_class = MovieSerializer

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return ProductsValidatorsCreate
        return self.serializer_class


class ProductsDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Products.objects.all()
    serializer_class = MovieSerializer

    def get_serializer_class(self):
        if self.request.method == 'PUT':
            return ProductsDetailValidatorCreate
        return self.serializer_class


class ReviewListAPIView(ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class ReviewDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class ReviewMoviesView(ListAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsReviewSerializer

#
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from rest_framework import status
# from .models import *
# from .serlializers import *
#
#
# @api_view(['GET'])
# def test(request):
#     dict_ = {
#         'text': "hello world",
#     }
#     return Response(data=dict_)
#
#
# @api_view(['GET'])
# def product_list_api_view(request):
#     products = Products.objects.all()
#     serializer = ProductSerializer(products, many=True)
#     return Response(data=serializer.data)
#
#
# @api_view(['GET'])
# def product_detail_api_view(request, id):
#     try:
#         products = Products.objects.get(id=id)
#     except Products.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#     serializer = ProductSerializer(products)
#     return Response(data=serializer.data)
#
#
# @api_view(['GET'])
# def categories_list_api_view(request):
#     category = Category.objects.all()
#     serializer = CategorySerializer(category, many=True)
#     return Response(data=serializer.data)
#
#
# @api_view(['GET'])
# def categories_detail_api_view(request, id):
#     try:
#         category = Category.objects.get(id=id)
#     except Category.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#     serializer = CategorySerializer(category)
#     return Response(data=serializer.data)
#
#
# @api_view(['GET'])
# def review_list_api_view(request):
#     review = Review.objects.all()
#     serializer = ReviewSerializer(review, many=True)
#     return Response(data=serializer.data)
#
#
# @api_view(['GET'])
# def review_detail_api_view(request, id):
#     try:
#         review = Review.objects.get(id=id)
#     except Review.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#     serializer = ReviewSerializer(review)
#     return Response(data=serializer.data)
