from django.shortcuts import render, get_object_or_404, redirect
from student.models import Student, Result
from django.http import HttpResponse
from django.template import loader
from django.db.models import ExpressionWrapper, Avg, Sum, FloatField, Count

import time

from rest_framework import viewsets
from student.models import Semester, Subject, Student, Result
from student.serializers import SemesterSerializer, StudentSerializer, SubjectSerializer, ResultSerializer

#  Student list view
def student_list(request):
    template = loader.get_template("student.html")
    return HttpResponse(template.render({}, request))
    


# def student_results(request):
    usn = request.GET.get('usn')
    semester = request.GET.get('semester')

    semester = int(semester)

    student = get_object_or_404(Student, USN=usn)

    if semester > student.current_sem:
        return HttpResponse("Given Semester is greater than current semester")

    if not Result.objects.filter(student=student, semester_id=semester).exists():
        return HttpResponse("Invalid values: No results found for this semester")

    results = (Result.objects.filter(student=student, semester_id=semester).values('semester__id').annotate(SGPA=ExpressionWrapper(Sum('marks') / Count('subject'), output_field=FloatField())))
    # print(results)
    for result in results:
        subjects = Result.objects.filter(student=student, semester_id=result['semester__id']).values('subject__name', 'marks')
        # result["subjects"] = [{"name": s["subject__name"], "marks": s["marks"]} for s in subjects]
        result["subjects"] = []
        for s in subjects:
            subject_data = {  
            "name": s["subject__name"],  
            "marks": s["marks"]
            }  
            result["subjects"].append(subject_data)

    # total_cgpa = (
    #     Result.objects.filter(student=student, semester_id__lte=semester)
    #     .values('semester__id')
    #     .annotate(SGPA=ExpressionWrapper(Sum('marks') / Count('subject'), output_field=FloatField()))
    #     .aggregate(CGPA=Avg('SGPA'))['CGPA']
    # )

    template = loader.get_template('results.html')
    context = {
        "student": student,
        "results": results,
        # "total_cgpa": total_cgpa,
    }
    return HttpResponse(template.render(context, request))


def student_results(request):

    allowed_parameters = {'usn','semester'}

    unexpected_params = set(request.GET.keys()) - allowed_parameters
    if unexpected_params:
        return HttpResponse(f"Invalid query parameters: {unexpected_params}")
    
    
    usn = request.GET.get('usn')
    semester = request.GET.get('semester')

    usn_value = Student.objects.filter(USN=usn)
    # print(usn_value)
    
    if len(usn_value)==0:
        return HttpResponse("""<script>
        alert("invalid usn");
        window.location.replace("http://localhost:8000/student/")
    </script>""")

        
    if not semester or not semester.isdigit():
        return HttpResponse("""<script>
        alert("invalid data");
        window.location.replace("http://localhost:8000/student/")
    </script>""")

        # return HttpResponse("<script>alert('invalid');</script>")
        

    semester = int(semester)

    if semester < 1 or semester > 8:
        return HttpResponse("Invalid semester: Please enter a number between 1 and 8.")

    student = get_object_or_404(Student, USN=usn)

    if semester > student.current_sem:
        return HttpResponse("Given Semester is greater than current semester")

    if not Result.objects.filter(student=student, semester_id=semester).exists():
        return HttpResponse("Invalid values: No results found for this semester")

    results = (Result.objects.filter(student=student, semester_id=semester).values('semester__id').annotate(SGPA=ExpressionWrapper(Sum('marks') / Count('subject'), output_field=FloatField())))

    for result in results:
        subjects = Result.objects.filter(student=student, semester_id=result['semester__id']).values('subject__name', 'marks')
        # result["subjects"] = [{"name": s["subject__name"], "marks": s["marks"]} for s in subjects]
        result["subjects"] = []
        for s in subjects:
            subject_data = {  
            "name": s["subject__name"],  
            "marks": s["marks"]
            }  
            result["subjects"].append(subject_data)

    template = loader.get_template('results.html')
    context = {
        "student": student,
        "results": results,
    }
    return HttpResponse(template.render(context, request))



class SemesterViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Semester.objects.all().order_by('id')
    serializer_class = SemesterSerializer


class SubjectViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Departments to be viewed or edited.
    """
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer

class StudentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Departments to be viewed or edited.
    """
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class ResultViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Departments to be viewed or edited.
    """
    queryset = Result.objects.all()
    serializer_class = ResultSerializer


