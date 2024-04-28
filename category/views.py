from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Category
from rest_framework import generics
from .serializers import CategorySerializer


class CategoryListView1(APIView):
    def get(self, request, level, format=None):
        category = Category.objects.filter(level=level)
        serializer = CategorySerializer(category, many=True)
        return Response(serializer.data)


class CategoryListView2(APIView):
    def get(self, request, level, parent, format=None):
        category = Category.objects.filter(level=level, parent=parent)
        serailizer = CategorySerializer(category, many=True)
        return Response(serailizer.data)


class CategoryListView3(APIView):
    def get(self, request, level, parent, format=None):
        category = Category.objects.filter(level=level, parent=parent)
        serailizer = CategorySerializer(category, many=True)
        return Response(serailizer.data)