from rest_framework import serializers
from .models import Student,Section,Items,Product

class SectionSerializer(serializers.ModelSerializer):
    class Meta:
        model=Section
        fields='__all__'


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields='__all__'

class productSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields='__all__'


class ItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Items
        fields='__all__'