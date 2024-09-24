from django.shortcuts import render, get_object_or_404, redirect
from .models import Category
from .forms import CategoryForm
from module_group.models import ModuleGroup

# Category views
def category_list(request):
    categories = Category.objects.filter(parent_categories__isnull=True)  # Only get categories that are not subcategories
    subcategories = Category.objects.filter(parent_categories__isnull=False).distinct()  # Subcategories

    return render(request, 'category_list.html', {
        'categories': categories,
        'subcategories': subcategories,
    })


def category_detail(request, pk):
    category = get_object_or_404(Category, pk=pk)
    return render(request, 'category_detail.html', {'category': category})

def category_add(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            category = form.save(commit=False)
            category.save()
            form.save_m2m()  # Lưu quan hệ many-to-many
            return redirect('category:category_list')  # Sử dụng đúng tên không gian
    else:
        form = CategoryForm()
    return render(request, 'category_form.html', {'form': form})


def category_edit(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            category = form.save(commit=False)
            category.save()
            form.save_m2m()  # Save many-to-many relations
            return redirect('category:category_list')
    else:
        form = CategoryForm(instance=category)
    return render(request, 'category_form.html', {'form': form})


def category_delete(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        category.delete()
        return redirect('category:category_list')
    return render(request, 'category_confirm_delete.html', {'category': category})
