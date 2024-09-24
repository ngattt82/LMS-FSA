from django.shortcuts import render, get_object_or_404, redirect
from .models import TrainingProgram, Subject, TrainingProgramSubjects
from .forms import TrainingProgramSubjectsForm

# Create your views here.
def manage_subjects(request, program_id):
    program = get_object_or_404(TrainingProgram, pk=program_id)
    if request.method == 'POST':
        form = TrainingProgramSubjectsForm(request.POST, instance=program)
        if form.is_valid():
            form.save(program)
            return redirect('training_program:training_program_list')
    else:
        form = TrainingProgramSubjectsForm(instance=program)
    return render(request, 'manage_subjects.html', {'form': form, 'program': program})

def view_subjects(request, program_id):
    program = get_object_or_404(TrainingProgram, pk=program_id)
    subjects = TrainingProgramSubjects.objects.filter(program=program).order_by('semester')
    return render(request, 'view_subjects.html', {'program': program, 'subjects': subjects})

def training_program_view(request, pk):
    program = get_object_or_404(TrainingProgram, pk=pk)
    return render(request, 'training_program_view.html', {'program': program})

