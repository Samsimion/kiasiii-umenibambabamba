from rest_framework import serializers
from .models import SchoolCategory, PrimarySchool,HighSchool

class SchoolCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SchoolCategory
        fields = '__all__'

class PrimarySchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrimarySchool
        fields = '__all__'

class HighSchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = HighSchool
        fields = '__all__'
