from rest_framework import serializers
from .models import *

class userSerializers(serializers.ModelSerializer):
    class Meta:
        model =  user
        fields = "__all__"

class productSerializers(serializers.ModelSerializer):
    class Meta:
        model =  product
        fields = "__all__"