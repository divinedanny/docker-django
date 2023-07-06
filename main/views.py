from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .serializers import (
    AddNoteSerializer,
    ViewAllNoteSerializer,
    ViewOneNoteSerializer,
)
from .models import Notes
from rest_framework import status
from rest_framework import generics

# Create your views here.

class HealthCheckView(generics.GenericAPIView):
    
    def get(self,request):
        return Response({'status':'status is ok'}, status=status.HTTP_200_OK)

class CreateNoteView(generics.CreateAPIView):
    serializer_class = AddNoteSerializer
    
    def post(self, request):
        serilizer = self.serializer_class(data=request.data, context={'request': request})
        serilizer.is_valid(raise_exception=True)
        
        serilizer.save()
        
        note = serilizer.data
        
        return Response(note, status=status.HTTP_201_CREATED)
    
class ViewAllNotesView(generics.ListAPIView):
    serializer_class = ViewAllNoteSerializer
    
    def get(self,request):
        data = Notes.objects.all()
        serializer = self.get_serializer(data, many=True)
        data = serializer.data
        return Response({
            'note': data
            }, status=status.HTTP_200_OK)
    
class ViewOneNoteView(generics.RetrieveAPIView):
    serializer_class = ViewOneNoteSerializer
    
    def get(self,request, id):
        note = Notes.objects.get(id=id)
        serializer = self.get_serializer(note)
        data = serializer.data
        
        return Response(data, status=status.HTTP_200_OK)        
        