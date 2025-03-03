from django.urls import path
from student.views import student_list, student_results

urlpatterns = [
    path('student/', student_list, name='student_list'),
    path('results/', student_results, name='student_results'),
]