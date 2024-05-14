from rest_framework import serializers 
from APIrest.models import Department, Employee

class DepartmentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Department
        feilds = ('DepartmentId', 'DepartmentName')

class APIrestSerializer(serializers. ModelSerializer):
    class Meta:
        model=Employee
        fields=('EmployeeId','EmployeeName','Department','DataOfJoining','PhotoFileName')