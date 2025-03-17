"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from employee import views as e
from product import views as p
from student import views as s


router = routers.DefaultRouter()
router.register(r'employees', e.EmployeeViewSet)
router.register(r'departments', e.DepartmentViewSet)
router.register(r'location', e.LocationViewSet)
router.register(r'contact', e.ContactViewSet)
router.register(r'brand', p.BrandViewSet)
router.register(r'categories', p.CategoryViewSet)
router.register(r'product', p.ProductViewSet)
router.register(r'semester', s.SemesterViewSet)
router.register(r'student', s.StudentViewSet)
router.register(r'subject', s.SubjectViewSet)
router.register(r'result', s.ResultViewSet)

# urlpatterns = [
#     path('', include(router.urls)),
#         path('', include('student.urls')),

#     path('departments/<int:department_id>/employees/', e.DepartmentEmployeeViewSet.as_view({'get': 'list'})),
#     path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
# ]




urlpatterns = [
    path('admin/', admin.site.urls),
    path('employees/',include('employee.urls')),
    path('', include('student.urls')),
    path('',include('product.urls')),
]

