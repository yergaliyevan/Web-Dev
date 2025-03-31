from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Product, Category
from .serializers import ProductSerializer, CategorySerializer

class ProductList(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

class ProductDetail(APIView):
    def get_object(self, id):
        try:
            return Product.objects.get(pk=id)
        except Product.DoesNotExist:
            return None

    def get(self, request, id):
        product = self.get_object(id)
        if product:
            serializer = ProductSerializer(product)
            return Response(serializer.data)
        return Response(status=status.HTTP_404_NOT_FOUND)

class CategoryList(APIView):
    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)

class CategoryDetail(APIView):
    def get_object(self, id):
        try:
            return Category.objects.get(pk=id)
        except Category.DoesNotExist:
            return None

    def get(self, request, id):
        category = self.get_object(id)
        if category:
            serializer = CategorySerializer(category)
            return Response(serializer.data)
        return Response(status=status.HTTP_404_NOT_FOUND)

class CategoryProducts(APIView):
    def get_object(self, id):
        try:
            return Category.objects.get(pk=id)
        except Category.DoesNotExist:
            return None

    def get(self, request, id):
        category = self.get_object(id)
        if category:
            products = category.products.all()  
            serializer = ProductSerializer(products, many=True)
            return Response(serializer.data)
        return Response(status=status.HTTP_404_NOT_FOUND)