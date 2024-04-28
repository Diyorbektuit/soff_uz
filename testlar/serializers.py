from rest_framework.serializers import ModelSerializer
from .models import Test
from .models import Question


class TestSerializer(ModelSerializer):
    class Meta:
        model = Test
        fields = '__all__'


class QuestionSerializer(ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'

