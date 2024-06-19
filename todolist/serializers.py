from rest_framework import serializers
from todolist.models import TodoItem

class TodoItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoItem
        fields = '__all__'
        extra_kwargs = {
            'author': {'required': False}  # Macht das author-Feld nicht erforderlich
        }

    def create(self, validated_data):
        request = self.context.get('request')
        validated_data['author'] = request.user
        return super().create(validated_data)