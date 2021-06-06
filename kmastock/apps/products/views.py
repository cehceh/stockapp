from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from .forms import ProductForm
from .models import Product

import os
import pyqrcode
from pyzbar.pyzbar import decode
from PIL import Image
from django.contrib.admin.views.decorators import staff_member_required
# Create your views here.

@staff_member_required
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST or None, request.FILES or None)
        # uuid = None
        if form.is_valid():
            barcode_value = request.POST.get('barurl')
            if barcode_value == None or barcode_value == '':
                messages.success(request, 'Create barcode without value is not valid')
            elif barcode_value != None:
                qr = pyqrcode.create(barcode_value)
                name = request.POST.get('name')
                img_name = '-'.join(name.split())
                file_path = 'media_root/barcodes/' + str(img_name) + '.png'
                print('file_path== '+str(file_path))
                match = Product.objects.filter(name=name).exists()
                uuid = None #  request.POST.get('barcode')
                if not os.path.exists(file_path) and not match:
                    qr.png('media_root/barcodes/' + str(img_name) + '.png', scale=8)
                    save_form = form.save(commit=False)
                    save_form.barimg = 'barcodes/' + str(img_name) + '.png' 
                    save_form.barurl = barcode_value
                    save_form.user = request.user
                    save_form.updateduser = request.user
                    # save_form.name = request.POST.get('name')
                    # match = Product.objects.product_already_exists(save_form.name)
                    save_form.save()

                    uuid = save_form.barcode
                    product_name = save_form.name 
                    product_id = save_form.id
                    messages.success(request, 'Product (' + str(product_name) + ') created successfully')
                    return redirect(reverse('products:edit_product', args=(product_id,)))
                else:
                    messages.success(request, 'Barcode is already exists or product name is repeated')
                    return redirect(reverse('products:add_product'))
    else:
        form = ProductForm()

    lastid = Product.objects.values('id').last()
    if lastid is not None:
        last = lastid['id'] + 1
    else:
        last = 1
    
    pro_name = request.POST.get('name')
    if pro_name is not None:
        join_name = '-'.join(pro_name.split())
    else:
        join_name = 'NoName'
    context = {
        'form': form,
        'lastid': last,
        'name':join_name,
        # 'uuid': uuid,
    }  
    return render(request, 'products/add_product.html', context)

# @login_required
def edit_product(request, product_id):
    qs = Product.objects.get_product_by_id(id=product_id) # get the product name
    # print(qs)
    form = ProductForm(request.POST or None, request.FILES or None, instance=qs)
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

