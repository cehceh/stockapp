from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import StocksForm
from .models import Stock

# Create your views here.
@login_required
def add_stock(request):
    if request.method == 'POST':
        form = StocksForm(request.POST or None)
        if form.is_valid():
            save_form = form.save(commit=False)
            save_form.save()
            name = save_form.name 
            stock_id = save_form.id
            messages.success(request, 'Create Stock (' + str(name) + ') done successfully')
            return redirect(reverse('stocks:edit_stock', args=(stock_id,)))
    else:
        form = StocksForm()
    context = {
        'form': form,
    }
        
    return render(request, 'stocks/add_stock.html', context)

@login_required
def edit_stock(request, stock_id):
    qs = Stock.objects.get_stock_by_id(id=stock_id) # get the stock name
    print(qs)
    form = StocksForm(request.POST or None, instance=qs)
    if form.is_valid():
        save_form = form.save()
        save_form.save() 
        name = save_form
        messages.success(request, 'Edit Stock (' + str(name) + ') done successfully')
        return redirect(reverse('stocks:edit_stock', args=(stock_id,)))
        # redirect(reverse('stocks:edit_stock', args=(stock_id,)))
        # redirect('stocks:edit_stock', kwargs={'id': stock_id})
    
    context = {
        'form': form,
        'stock_id':qs,
    }   
    return render(request, 'stocks/edit_stock.html', context)