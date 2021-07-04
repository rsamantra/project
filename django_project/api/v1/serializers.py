from rest_framework import (exceptions, serializers)
from core.models import *


class CreateItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = "__all__"
    
    def create(self, validated_data):
        item_obj = Item()
        item_obj.item = validated_data.get("item")
        item_obj.save()
        return item_obj