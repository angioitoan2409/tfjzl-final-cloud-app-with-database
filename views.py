from django.shortcuts import render
from .models import Course

def submit(request, course_id):
    # Logic to handle exam submission
    return render(request, 'onlinecourse/exam_result.html')

def show_exam_result(request, course_id):
    # Logic to display the results
    return render(request, 'onlinecourse/exam_result.html')
