from rest_framework import serializers
from .models import Notes



class AddNoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notes
        fields = '__all__'
        
        
    def create(self, validated_data):
        data = Notes.objects.create(**validated_data)
        data.save()
        return data
    

class ViewAllNoteSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Notes
        fields = '__all__'
        
    def get(self):
        
        data = Notes.objects.all()
        
        return data
    
class ViewOneNoteSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Notes
        fields = '__all__'
    
    def get(self, attrs):
        id = attrs['id']
        note = Notes.objects.get(id=id)
        
        return note 
    
   