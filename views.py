from django.shortcuts import render, get_object_or_404
from .models import Course, Enrollment, Submission, Choice

def submit(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    # Logic to retrieve course and enrollment
    enrollment = Enrollment.objects.get(user=request.user, course=course)
    # Create Submission object
    submission = Submission.objects.create(enrollment=enrollment)
    # Associate selected Choice objects
    if request.method == 'POST':
        selected_ids = request.POST.getlist('choice')
        for choice_id in selected_ids:
            choice = Choice.objects.get(pk=choice_id)
            submission.choices.add(choice)
            
    return render(request, 'onlinecourse/exam_result.html')

def show_exam_result(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    enrollment = Enrollment.objects.get(user=request.user, course=course)
    submission = Submission.objects.filter(enrollment=enrollment).last()
    
    # Calculate total_score and possible_score using is_get_score()
    total_score = 0
    possible_score = 100
    if submission:
        total_score = submission.is_get_score()
        
    context = {
        'course': course,
        'total_score': total_score,
        'possible_score': possible_score,
    }
    return render(request, 'onlinecourse/exam_result.html', context)
