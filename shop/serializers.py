from rest_framework import serializers
from shop.models import Product, Category
from django.contrib.auth import get_user_model

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()

        return user

    class Meta:
        model = User
        fields = ("id", "username", "password",)


class ProductTestSerializer(serializers.Serializer):
    name = serializers.CharField(max_length = 255)
    description = serializers.CharField(max_length=255)
    price = serializers.CharField(max_length=255)


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields = ('id','category')

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields = ('id','name','description', 'price', 'category')
