from django.shortcuts import render
from .serializers import TestSerializer, QuestionSerializer
from .models import Test, Question
from rest_framework import generics
# Create your views here.

class TestsList(generics.ListAPIView):
    queryset = Test.objects.all()
    serializer_class = TestSerializer


class TestDetail(generics.RetrieveAPIView):
    queryset = Test.objects.all()
    serializer_class = TestSerializer


class TestCreate(generics.CreateAPIView):
    queryset = Test.objects.all()
    serializer_class = TestSerializer


class TestUpdate(generics.UpdateAPIView):
    queryset = Test.objects.all()
    serializer_class = TestSerializer


class TestDetele(generics.DestroyAPIView):
    queryset = Test.objects.all()
    serializer_class = TestSerializer


class QuestionsList(generics.ListAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class QuestionDetail(generics.RetrieveAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class QuestionCreate(generics.CreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class QuestionUpdate(generics.UpdateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class QuestionDetele(generics.DestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

