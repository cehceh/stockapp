from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from .forms import ProductForm
from .models import Product
# Create your views here.

def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            save_form = form.save(commit=False)
            save_form.user = request.user
            save_form.updateduser = request.user
            save_form.name = request.POST.get('name')
            # save_form.description = request.POST.get('description')
            match = Product.objects.product_already_exists(save_form.name)
            if match:
                messages.success(request, 'Add product (' + str(save_form.name) + ') failed, It seems that product name already exists')
                return redirect(reverse('products:add_product'))
            else:
                save_form.save()
                name = save_form.name 
                product_id = save_form.id
                messages.success(request, 'Product (' + str(name) + ') created successfully')
                return redirect(reverse('products:edit_product', args=(product_id,)))
    else:
        form = ProductForm()

    context = {
        'form': form,
    }  
    return render(request, 'products/add_product.html', context)

# @login_required
def edit_product(request, product_id):
    qs = Product.objects.get_product_by_id(id=product_id) # get the product name
    # print(qs)
    form = ProductForm(request.POST or None, instance=qs)
    if form.is_valid():
        save_form = form.save()
        save_form.updateduser = request.user
        save_form.save() 
        name = save_form.name
        messages.success(request, 'Edit Product (' + str(name) + ') done successfully')
        return redirect(reverse('products:edit_product', args=(product_id,)))
            
    context = {
        'form': form,
        'product_id':qs,
    }   
    return render(request, 'products/edit_product.html', context)

