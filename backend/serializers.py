from django.db.models import fields
from rest_framework import serializers
from .models import*


class ApiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Posts
        fields = '__all__'
