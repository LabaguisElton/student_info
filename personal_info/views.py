from django.shortcuts import get_object_or_404, render

from .models import Student


def student_list(request):
    students = Student.objects.all()
    return render(request, 'personal_info/student_list.html', {'students': students})


def student_detail(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    return render(request, 'personal_info/student_detail.html', {'student': student})
