from django.shortcuts import render, get_object_or_404, redirect
from .models import User, UserProfile, Role
from .forms import UserForm, UserProfileForm
from django.db.models import Q
# User Views

def user_list(request):
    query = request.GET.get('q', '')
    selected_role = request.GET.get('role', '')

    users = User.objects.all()
    roles = Role.objects.all()

    if query and selected_role:
        users = users.filter(
            Q(full_name__icontains=query) | Q(username__icontains=query),
            role__role_name=selected_role
        )
    elif query: 
        users = users.filter(
            Q(full_name__icontains=query) | Q(username__icontains=query)
        )
    elif selected_role: 
        users = users.filter(role__role_name=selected_role)

    not_found = not users.exists()

    return render(request, 'user_list.html', {
        'users': users,
        'query': query,
        'roles': roles,
        'selected_role': selected_role,
        'not_found': not_found,
    })





def user_detail(request, pk):
    user = get_object_or_404(User, pk=pk)
    profile = user.profile if hasattr(user, 'profile') else None

    return render(request, 'user_detail.html', {'user': user, 'profile': profile})

def user_edit(request, pk):
    user = get_object_or_404(User, pk=pk)
    profile = UserProfile.objects.filter(user=user).first()  
    
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=user)
        profile_form = UserProfileForm(request.POST, instance=profile)
        
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            if profile:
                profile_form.save()
            else:
                profile = profile_form.save(commit=False)
                profile.user = user
                profile.save()
            return redirect('user:user_list')
    else:
        user_form = UserForm(instance=user)
        profile_form = UserProfileForm(instance=profile) if profile else UserProfileForm()
    
    return render(request, 'user_form.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })

def user_add(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = UserProfileForm(request.POST)
        
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            return redirect('user:user_list')
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()
    
    return render(request, 'user_form.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })

def user_delete(request, pk):
    user = get_object_or_404(User, pk=pk)
    
    if request.method == 'POST':
        user.delete()
        return redirect('user:user_list')  
    
    return render(request, 'user_confirm_delete.html', {'user': user})