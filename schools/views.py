from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import PrimarySchool,HighSchool,SchoolCategory
# Create your views here.

def register_primary_school(request):
    if request.method == 'POST':
        data = json.loads(request.body)

        try:
            category = SchoolCategory.objects.get(id = data['category'])
            school = PrimarySchool.objects.create(
                name = data['name'],
                category = category,
                school_type = data['school_type'],
                address = = data['address'],
                email = data['email'],
                phone = data[phone],
                is_approved = data.get('is_approved', False)

            )
            return JsonResponse({'message': 'Primary School registered successfully!'}, status = 201)
        
        except SchoolCategory.DoesNotExist:
            return JsonResponse({'error': 'Invalid Category'}, status = 400)
    
    return JsonResponse({'error': 'Invalid request method'}, status = 405)             

@csrf_exempt
def register_high_school(request):
    if request.method == 'POST':
        data = json.loads(request.body)

        try:
            category = SchoolCategory.objects.get(id =data['category'])
            school = HighSchool.objects.create(
                name = data['name'],
                category = category,
                school_type =data['school_type'],
                address = data['address'],
                email = data['email'],
                phone = data['phone'],
                is_approved = data.get('is_approved', False),
            )
            return JsonResponse({'message':'High School registered successfully!'}, status=201)
        except SchoolCategory.DoesNotExist:
             return JsonResponse({'error': 'Invalid category'}, status=400)

    return JsonResponse({'error': 'Invalid request method'}, status=405)
