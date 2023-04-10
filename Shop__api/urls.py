"""Shop__api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the iinclude() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# import product.views
# from django.contrib import admin
# from django.urls import path
# from product import views
#
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('api/v1/test/', views.test),
#     path('api/v1/products/', views.product_list_api_view),
#     path('api/v1/products/<int:id>/', views.product_detail_api_view),
#     path('api/v1/categorys/', views.categories_list_api_view),
#     path('api/v1/categorys/<int:id>/', views.categories_detail_api_view),
#     path('api/v1/reviews/', views.review_list_api_view),
#     path('api/v1/reviews/<int:id>/', views.review_detail_api_view),
#
# ]


from django.contrib import admin
from django.urls import path
from product.views import *
from user.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/directors/', CategoryListAPIView.as_view()),
    path('api/v1/directors/<int:pk>/', CategoryDetailAPIView.as_view()),
    path('api/v1/movies/', ProductsListAPIView.as_view()),
    path('api/v1/movies/<int:pk>/', ProductsDetailAPIView.as_view()),
    path('api/v1/reviews/', ReviewListAPIView.as_view()),
    path('api/v1/reviews/<int:pk>/', ReviewDetailAPIView.as_view()),
    path('api/v1/movies/reviews/', ReviewMoviesView.as_view()),
    path('api/v1/users/registration/', RegistrationAPIView.as_view()),
    path('api/v1/users/confirm/', ConfirmUserAPIView.as_view()),
    path('api/v1/users/authorization/', AuthorizationAPIView.as_view()),
]
