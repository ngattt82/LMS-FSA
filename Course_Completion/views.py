from django.shortcuts import HttpResponse,render, get_object_or_404, redirect
from .models import CourseCompletion
from .forms import CourseCompletionForm

# Create your views here.

def CourseCompletion_list(request):
    try:
        course = CourseCompletion.objects.all()
        return render(request, 'CourseCompletion_list.html', {'CourseCompletion':course})
    except Exception as e:
        return HttpResponse(f'error: {e}')
def Completed(request):
    pass