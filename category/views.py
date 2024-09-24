from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, SubCategory
from .forms import CategoryForm, SubCategoryForm
from module_group.models import ModuleGroup

# Category views
def category_list(request):
    categories = Category.objects.all()  # Get all categories
    subcategories = SubCategory.objects.all()  # Get all subcategories

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
        subcategory_form = SubCategoryForm(request.POST)

        if 'create_subcategory' in request.POST:
            if subcategory_form.is_valid():
                subcategory_form.save()
                return redirect('category:category_list')  # Redirect to category list

        elif form.is_valid():
            category = form.save(commit=False)
            category.save()  # Save the Category instance to get a primary key
            form.save_m2m()  # Save the many-to-many relationship
            return redirect('category:category_list')

    else:
        form = CategoryForm()
        subcategory_form = SubCategoryForm()

    return render(request, 'category_form.html', {
        'form': form,
        'subcategory_form': subcategory_form
    })

def category_delete(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        category.delete()
        return redirect('category:category_list')
    return render(request, 'category_confirm_delete.html', {'category': category})

# Xử lý sửa Category
def category_edit(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('category_list')
    else:
        form = CategoryForm(instance=category)
    return render(request, 'category_edit.html', {'form': form})