from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from APIrest.models import Department, Employee
from APIrest.serializers import DepartmentSerializers, Department
# Create your views here.


@csrf_exempt
def departmentAPI(request, id=0):
    if request.method =='GET':
        Departments = Departments.objectall()
        Departments_serializer = DepartmentSerializers(Departments,many = True)
        return JsonResponse(departments_serializer.data, safe = False)
    elif request.method =='POST':
        department_data = JSONParser().parse(request)
        departments_serializer=DepartmentSerializers(data = department_data)
        if departments_serializer.is_valid():
            departments_serializer.save()
            return JsonResponse("Added Succesfully",safe=False)
        return JsonResponse("Failed to Add", safe=False)
    elif request.method == 'PUT':
        department_data= JSONParser().parse(request)
        department=Departments.object.get(DepartmentId=department_data['Department'])
        departments_serializer=DepartmentSerializers(department,fdata=department_data)
        if departments_serializer.is_valid():
            departments_serializer.save()
            return JsonResponse("Update succesfully", safe=False)
        return JsonResponse("Failed to Update")
    elif request.method == 'DELETE':
        department=Departments.objects.get(DepartmentId=Id)
        department.delete()
    return JsonResponse("Delete Succesfully",safe=False)