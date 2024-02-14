from rest_framework import serializers
from .models import CourseModel
from rest_framework.validators import ValidationError

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseModel
        fields = '__all__'

    def validate_day(self,d):
        if d<0:
            raise ValidationError(
                {
                    'status':False,
                    'message':"Manfiy son kiritib bo`lmaydi"
                }
            )

class CourseUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseModel
        fields = '__all__'