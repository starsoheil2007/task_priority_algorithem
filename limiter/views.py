from .models import *
from .serializers import UserProcessQueueSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


# Create your views here.

class ProcessList(APIView):
    """
    List all process, or create a new process.
    """

    def get(self, request):
        """
        Get List of process
        """
        all_process = UserProcessQueue.objects.all()
        serializer = UserProcessQueueSerializer(all_process, many=True)
        return Response(serializer.data)

    def post(self, request):
        """
        Send new process
        @params:
            user_id (integer): Id of user
            x (integer): time to process on user
        """
        user_id = request.data.get("user_id", None)
        time_to_complete = request.data.get("x", None)
        if not user_id or not time_to_complete:
            return Response("Your data in incomplete", status=status.HTTP_400_BAD_REQUEST)
        try:
            user = Users.objects.get(pk=user_id)
            UserProcessQueue.objects.create(user=user, time_to_complete=time_to_complete, is_stopped=True)
        except Users.DoesNotExist:
            return Response("This user not found", status=status.HTTP_404_NOT_FOUND)
        return Response("Your process created successfully", status=status.HTTP_201_CREATED)
