from django.shortcuts import render, get_object_or_404, redirect
from .models import DiscussionThread,ThreadComments
from .forms import ThreadForm,CommentForm

def thread_list(request):
    threads = DiscussionThread.objects.all()
    return render(request, 'thread/thread_list.html', {'threads': threads})


def createThread(request):
    if request.method == 'POST':
        form = ThreadForm(request.POST)
        if form.is_valid():
            thread = form.save(commit=False)
            thread.save()
            return redirect('thread:thread_list')  
        else:
            print(f"Form errors: {form.errors}")
    else:
        form = ThreadForm()

    return render(request, 'thread/thread_form.html', {'form': form})


def updateThread(request, pk):
    thread = get_object_or_404(DiscussionThread, pk=pk)
    if request.method == 'POST':
        form = ThreadForm(request.POST, instance=thread)
        if form.is_valid():
            form.save()
            return redirect('thread:thread_list')
    else:
        form = ThreadForm(instance=thread)
    return render(request, 'thread/thread_form.html', {'form': form})

def deleteThread(request, pk):
    thread = get_object_or_404(DiscussionThread, pk=pk)
    if request.method == 'POST':
        thread.delete()
        return redirect('thread:thread_list')
    return render(request, 'thread/thread_confirm_delete.html', {'thread': thread})

def thread_detail(request, pk):
    thread = get_object_or_404(DiscussionThread, pk=pk)
    return render(request, 'thread/thread_detail.html', {'thread': thread})

def add_comment(request,pk):
    thread = get_object_or_404(DiscussionThread,pk = pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.thread = thread
            comment.save()
            return redirect('thread:thread_detail',pk = thread.pk)
    else:
        form - CommentForm()
    
    return render(request,'thread/thread_detail.html',{'thread': thread, 'form': form})

def update_comment(request, pk, comment_id):
    comment = get_object_or_404(ThreadComments, pk=comment_id)
    
    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect('thread:thread_detail', pk=pk)
    else:
        form = CommentForm(instance=comment)

    return render(request, 'thread/comment_form.html', {'form': form,'comment': comment,})

def delete_comment(request, pk, comment_id):
    thread = get_object_or_404(DiscussionThread, pk=pk)
    comment = get_object_or_404(ThreadComments, pk=comment_id, thread=thread)
    
    if request.method == 'POST':
        comment.delete()
        return redirect('thread:thread_detail', pk=thread.pk)  # Redirect back to the thread's detail page
    
    return render(request, 'thread/comment_confirm_delete.html', {'comment': comment})
