from rest_framework import serializers
from .models import UserProcessQueue


class UserProcessQueueSerializer(serializers.ModelSerializer):
    """
    Serializer for show tasks
    """

    class Meta:
        model = UserProcessQueue
        fields = ['user_id', '__str__', 'time_to_complete', 'time_completed', 'is_finished', 'is_stopped']
