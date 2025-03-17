from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader

from rest_framework import permissions, viewsets

from employee.models import Employee, Department, Location, Contact_details
from employee.serializers import EmployeeSerializer, DepartmentSerializer, LocationSerializer, ContactSerializer


# Create your views here.


def index(request):
    employee_id = request.GET.get("id")
    email = request.GET.get("email")
    designation = request.GET.get("designation")

    if employee_id:
        employees = Employee.objects.filter(id=employee_id)
    else:
        employees = Employee.objects.all().order_by("id")

    if email:
        employees = employees.filter(email=email)
        
    if designation:
        employees = employees.filter(designation=designation)

    return render(request, "index.html", {"employees": employees, "all_employees": Employee.objects.all()})

def employee_detail(request, employee_id):
    employee = Employee.objects.filter(id=employee_id).first()
    return render(request, "employee_detail.html", {"employee": employee})




class DepartmentEmployeeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows employees to be viewed or edited.
    """
    serializer_class = EmployeeSerializer

    def get_queryset(self):
        department_id = self.kwargs.get('department_id')
        if department_id:
            return Employee.objects.filter(department_id=department_id)
        return Employee.objects.none()




class EmployeeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Employee.objects.all().order_by('id')
    serializer_class = EmployeeSerializer


class DepartmentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Departments to be viewed or edited.
    """
    queryset = Department.objects.all().order_by('name')
    serializer_class = DepartmentSerializer

class LocationViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Departments to be viewed or edited.
    """
    queryset = Location.objects.all().order_by('name')
    serializer_class = LocationSerializer

class ContactViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Departments to be viewed or edited.
    """
    queryset = Contact_details.objects.all()
    serializer_class = ContactSerializer

