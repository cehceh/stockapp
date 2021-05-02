from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from .forms import CategoryForm
from .models import Categories
from kmastock.utils import auth_user_required
# Create your views here.

@auth_user_required
def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST or None)
        if form.is_valid():
            save_form = form.save(commit=False)
            save_form.user = request.user
            save_form.updateduser = request.user
            save_form.name = request.POST.get('name')
            save_form.description = request.POST.get('description')
            match = Categories.objects.filter().category_already_exists(save_form.name)
            if match:
                messages.success(request, 'Add category (' + str(save_form.name) + ') failed, It seems that category name already exists')
                return redirect(reverse('category:add_category'))
            else:
                save_form.save()
                name = save_form.name 
                category_id = save_form.id
                messages.success(request, 'Category (' + str(name) + ') created successfully')
                return redirect(reverse('category:edit_category', args=(category_id,)))
    else:
        form = CategoryForm()

    context = {
        'form': form,
    }  
    return render(request, 'category/add_category.html', context)

@auth_user_required
def edit_category(request, category_id):
    qs = Categories.objects.get_category_by_id(id=category_id) # get the category name
    # print(qs)
    form = CategoryForm(request.POST or None, instance=qs)
    if form.is_valid():
        save_form = form.save()
        save_form.updateduser = request.user
        save_form.save() 
        name = save_form.name
        messages.success(request, 'Edit Category (' + str(name) + ') done successfully')
        return redirect(reverse('category:edit_category', args=(category_id,)))
            
    context = {
        'form': form,
        'category_id':qs,
    }   
    return render(request, 'category/edit_category.html', context)

