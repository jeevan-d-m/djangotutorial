from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from employee.models import Employee
from django.template import loader

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
