from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Smartphone
from .serializers import SmartphoneSerializer

class SmartphoneListAPIView(APIView):
    def get(self, request):
        phones = Smartphone.objects.all()
        serializer = SmartphoneSerializer(phones, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = SmartphoneSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)