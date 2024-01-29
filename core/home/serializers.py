from rest_framework import serializers
from .models import *


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student 
        #fields = ['name', 'age']
        # exclude = ['id', ] // je field remove korte chai
        fields = "__all__"


    def validate(self, data):
        if data['age'] < 18:
            raise serializers.ValidationError({"error" : "age can not be less than 18"})
        return data
    def validate(self, data):
        if data['name']:
            for n in data['name']:
                if n.isdigit():
                    raise serializers.ValidationError({"error" : "name can not contain any digit"})
        return data