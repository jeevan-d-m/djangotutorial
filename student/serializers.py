from rest_framework import serializers
from student.models import Student, Semester, Subject, Result

class SemesterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Semester
        fields = ['id']

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ['name']


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['USN','name','current_sem']

    def validate_current_sem(self, value):
        if value<1 or value>8:
            raise serializers.ValidationError("Sem out of range")



class ResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = Result
        fields = ['subject','semester','student','marks']