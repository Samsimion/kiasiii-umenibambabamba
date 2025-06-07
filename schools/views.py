from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import PrimarySchool, HighSchool
from .serializers import PrimarySchoolSerializer, HighSchoolSerializer

@api_view(['GET', 'POST'])
def primary_schools(request):
    if request.method == 'GET':
        schools = PrimarySchool.objects.all()
        serializer = PrimarySchoolSerializer(schools, many=True)  # Fix: many=True not 'True'
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = PrimarySchoolSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Primary School registered successfully!'}, status=201)
        return Response(serializer.errors, status=400)  # Fix: serializer.errors not error

@api_view(['GET', 'POST'])
def high_schools(request):  # Fix: better to name it high_schools for consistency
    if request.method == 'GET':
        schools = HighSchool.objects.all()
        serializer = HighSchoolSerializer(schools, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = HighSchoolSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'High School registered successfully!'}, status=201)
        return Response(serializer.errors, status=400)
