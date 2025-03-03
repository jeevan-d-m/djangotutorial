from django.shortcuts import render, get_object_or_404
from student.models import Student, Result
from django.http import HttpResponse, HttpResponseNotFound
from django.template import loader
from django.db.models import ExpressionWrapper, Avg, Sum, FloatField, Count


#  Student list view
def student_list(request):
    template = loader.get_template("student.html")
    return HttpResponse(template.render({}, request))
    


def student_results(request):
    usn = request.GET.get('usn')
    semester = request.GET.get('semester')

    semester = int(semester)

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

    total_cgpa = (
        Result.objects.filter(student=student, semester_id__lte=semester)
        .values('semester__id')
        .annotate(SGPA=ExpressionWrapper(Sum('marks') / Count('subject'), output_field=FloatField()))
        .aggregate(CGPA=Avg('SGPA'))['CGPA']
    )

    template = loader.get_template('results.html')
    context = {
        "student": student,
        "results": results,
        "total_cgpa": total_cgpa,
    }
    return HttpResponse(template.render(context, request))

