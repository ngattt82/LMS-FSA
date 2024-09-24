from django.shortcuts import render, redirect, get_object_or_404
from .forms import CollaborationGroupForm
from .models import CollaborationGroup
from collaboration_member.models import GroupMember
from user.models import User  # Import the User model

def collaboration_group_list(request):
    collaboration_groups = CollaborationGroup.objects.all()
    return render(request, 'collaboration_group_list.html', {'collaboration_groups': collaboration_groups})

def collaboration_group_add(request):
    if request.method == 'POST':
        form = CollaborationGroupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('collaboration_group:collaboration_group_list')
    else:
        form = CollaborationGroupForm()
    return render(request, 'collaboration_group/collaboration_group_form.html', {'form': form})

def collaboration_group_edit(request, pk):
    collaboration_group = get_object_or_404(CollaborationGroup, pk=pk)
    if request.method == 'POST':
        form = CollaborationGroupForm(request.POST, instance=collaboration_group)
        if form.is_valid():
            form.save()
            return redirect('collaboration_group:collaboration_group_list')
    else:
        form = CollaborationGroupForm(instance=collaboration_group)
    return render(request, 'collaboration_group_form.html', {'form': form})

def collaboration_group_delete(request, pk):
    collaboration_group = get_object_or_404(CollaborationGroup, pk=pk)
    if request.method == 'POST':
        collaboration_group.delete()
        return redirect('collaboration_group:collaboration_group_list')
    return render(request, 'collaboration_group_confirm_delete.html', {'collaboration_group': collaboration_group})

def manage_group(request, group_id):
    group = get_object_or_404(CollaborationGroup, pk=group_id)
    members = GroupMember.objects.filter(group=group)
    all_users = User.objects.exclude(id__in=members.values_list('user_id', flat=True))

    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        if user_id:
            user = get_object_or_404(User, pk=user_id)
            GroupMember.objects.create(group=group, user=user)
            return redirect('collaboration_group:manage_group', group_id=group.id)

    return render(request, 'manage_group.html', {
        'group': group,
        'members': members,
        'all_users': all_users,
    })
from django.shortcuts import get_object_or_404, redirect
from collaboration_member.models import GroupMember

def remove_member(request, group_id, member_id):
    member = get_object_or_404(GroupMember, pk=member_id, group_id=group_id)
    member.delete()
    return redirect('collaboration_group:manage_group', group_id=group_id)
