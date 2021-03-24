from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from .forms import VendorsForm
from .models import Vendor
# Create your views here.

def add_vendor(request):
    if request.method == 'POST':
        form = VendorsForm(request.POST or None)
        if form.is_valid():
            save_form = form.save(commit=False)
            save_form.user = request.user
            save_form.updateduser = request.user
            save_form.name = request.POST.get('name')
            save_form.description = request.POST.get('description')
            match = Vendor.objects.filter().vendor_already_exists(save_form.name)
            if match:
                messages.success(request, 'Add vendor (' + str(save_form.name) + ') failed, It seems that vendor name already exists')
                return redirect(reverse('vendors:add_vendor'))
            else:
                save_form.save()
                name = save_form.name 
                vendor_id = save_form.id
                messages.success(request, 'Vendor (' + str(name) + ') created successfully')
                return redirect(reverse('vendors:edit_vendor', args=(vendor_id,)))
    else:
        form = VendorsForm()

    context = {
        'form': form,
    }  
    return render(request, 'vendors/add_vendor.html', context)

# @login_required
def edit_vendor(request, vendor_id):
    qs = Vendor.objects.get_vendor_by_id(id=vendor_id) # get the vendor name
    # print(qs)
    form = VendorsForm(request.POST or None, instance=qs)
    if form.is_valid():
        save_form = form.save()
        save_form.updateduser = request.user
        save_form.save() 
        name = save_form.name
        messages.success(request, 'Edit Vendor (' + str(name) + ') done successfully')
        return redirect(reverse('vendors:edit_vendor', args=(vendor_id,)))
            
    context = {
        'form': form,
        'vendor_id':qs,
    }   
    return render(request, 'vendors/edit_vendor.html', context)

