from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Assignment, Submission
from .forms import AssignmentForm, SubmissionForm, GradingForm
from module_group.models import ModuleGroup

def assignment_list(request):
    assignments = Assignment.objects.all().order_by('-start_date')  # Order by start date, most recent first
    module_groups = ModuleGroup.objects.all()

    # Add submission information to each assignment
    for assignment in assignments:
        assignment.submission_count = Submission.objects.filter(assignment=assignment).count()
        # Add user's submission if exists
        user_submission = Submission.objects.filter(assignment=assignment, student=request.user).first()
        assignment.user_submission = user_submission
        assignment.user_grade = user_submission.grade if user_submission else None

    return render(request, 'assignment_list.html', {'assignments': assignments, 'module_groups': module_groups})

def create_assignment(request):
    if request.method == 'POST':
        form = AssignmentForm(request.POST)
        if form.is_valid():
            assignment = form.save(commit=False)
            assignment.created_by = request.user
            assignment.save()
            messages.success(request, 'Assignment created successfully.')
            return redirect('assignment:assignment_list')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = AssignmentForm()
    return render(request, 'create_assignment.html', {'form': form})

def edit_assignment(request, assignment_id):
    assignment = get_object_or_404(Assignment, id=assignment_id)
    if request.method == 'POST':
        form = AssignmentForm(request.POST, instance=assignment)
        if form.is_valid():
            form.save()
            messages.success(request, 'Assignment updated successfully.')
            return redirect('assignment:assignment_list')
    else:
        form = AssignmentForm(instance=assignment)
    return render(request, 'edit_assignment.html', {'form': form, 'assignment': assignment})

def delete_assignment(request, assignment_id):
    assignment = get_object_or_404(Assignment, id=assignment_id)
    if request.method == 'POST':
        assignment.delete()
        messages.success(request, 'Assignment deleted successfully.')
        return redirect('assignment:assignment_list')
    return render(request, 'delete_assignment.html', {'assignment': assignment})

def submit_assignment(request, assignment_id):
    assignment = get_object_or_404(Assignment, id=assignment_id)
    if request.method == 'POST':
        form = SubmissionForm(request.POST, request.FILES)
        if form.is_valid():
            submission = form.save(commit=False)
            submission.assignment = assignment
            submission.student = request.user
            submission.save()
            messages.success(request, 'Assignment submitted successfully.')
            return redirect('assignment:assignment_list')
    else:
        form = SubmissionForm()
    return render(request, 'submit_assignment.html', {'form': form, 'assignment': assignment})

def grade_submission(request, submission_id):
    submission = get_object_or_404(Submission, id=submission_id)
    if request.method == 'POST':
        form = GradingForm(request.POST, instance=submission)
        if form.is_valid():
            form.save()
            messages.success(request, 'Submission graded successfully.')
            return redirect('assignment:submission_detail', submission_id=submission.id)
    else:
        form = GradingForm(instance=submission)
    return render(request, 'grade_submission.html', {'form': form, 'submission': submission})

def submission_list(request, assignment_id):
    assignment = get_object_or_404(Assignment, id=assignment_id)
    submissions = Submission.objects.filter(assignment=assignment)
    return render(request, 'submission_list.html', {'assignment': assignment, 'submissions': submissions})

def view_grades(request):
    submissions = Submission.objects.filter(student=request.user)
    return render(request, 'view_grades.html', {'submissions': submissions})

def assignment_detail(request, assignment_id):
    assignment = get_object_or_404(Assignment, id=assignment_id)
    context = {
        'assignment': assignment,
        'user_is_creator': assignment.created_by == request.user
    }
    return render(request, 'assignment_detail.html', context)

# Add this new view
def submission_detail(request, submission_id):
    submission = get_object_or_404(Submission, id=submission_id)
    return render(request, 'submission_detail.html', {'submission': submission})
