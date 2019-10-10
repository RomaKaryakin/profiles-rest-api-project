from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from shop import serializers
from shop.models import Product, Category

from django.contrib.auth import get_user_model

User = get_user_model()

from .serializers import UserSerializer


products = [
    {
        'id': 1,
        'name': "Asd"
    },
    {
        'id': 2,
        'name': "Asd"
    }
]

#(ApiView) means Extends

class ProductView(APIView):

    serializers_class = serializers.ProductSerializer

    def get(self, request, format=None):
        products = Product.objects.all()
        serializer = self.serializers_class(products, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = self.serializers_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            Response({"msg": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

class ProductDetailViews(APIView):
    serializers_class = serializers.ProductSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self, pk):
        try:
            product = Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            return False
        return product

    def put(self, request, pk, format=None):
        product = self.get_queryset(pk)

        if not product:
            content ={
                'status': 'Not Found'
            }
            return Response(content, status.HTTP_404_NOT_FOUND)

        serializer = self.serializers_class(product, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response({"msg": serializer.errors}, status=status)

    def get(self, request, pk, format=None):
        product = self.get_queryset(pk)

        if not product:
            content ={
                'status': 'Not Found'
            }
            return Response(content, status.HTTP_404_NOT_FOUND)

        serializer = self.serializers_class(product)
        return Response(serializer.data)

    def delete(self, request, pk, format=None):
        product = self.get_queryset(pk)

        if not product:
            content ={
                'status': 'Not Found'
            }
            return Response(content, status.HTTP_404_NOT_FOUND)
        product.delete()
        return Response({'msg': 'No Content'}, status=status.HTTP_204_NO_CONTENT)



class CategoryView(APIView):

    serializers_class = serializers.CategorySerializer

    def get(self, request, format=None):
        categories = Category.objects.all()
        serializer = self.serializers_class(categories, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = self.serializers_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            Response({"msg": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

class CategoryDetailViews(APIView):
    serializers_class = serializers.CategorySerializer

    def get_queryset(self, pk):
        try:
            category = Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            return False
        return category

    def put(self, request, pk, format=None):
        category = self.get_queryset(pk)

        if not category:
            content ={
                'status': 'Not Found'
            }
            return Response(content, status.HTTP_404_NOT_FOUND)

        serializer = self.serializers_class(category, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response({"msg": serializer.errors}, status=status)

    def get(self, request, pk, format=None):
        category = self.get_queryset(pk)

        if not category:
            content ={
                'status': 'Not Found'
            }
            return Response(content, status.HTTP_404_NOT_FOUND)

        serializer = self.serializers_class(category)
        return Response(serializer.data)

    def delete(self, request, pk, format=None):
        category = self.get_queryset(pk)

        if not category:
            content ={
                'status': 'Not Found'
            }
            return Response(content, status.HTTP_404_NOT_FOUND)
        category.delete()
        return Response({'msg': 'No Content'}, status=status.HTTP_204_NO_CONTENT)


class CreateUserView(CreateAPIView):

    model = get_user_model()
    permission_classes = [
        AllowAny
    ]
    serializer_class = UserSerializer
