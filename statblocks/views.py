from django.shortcuts import render, redirect
from .models import Statblock, Trait
from django.contrib.auth.decorators import login_required
from . import forms

# Create your views here.
def statblocks_list(request):
    statblocks = Statblock.objects.all().order_by('name')
    return render(request, 'statblocks/statblocks_list.html', {'statblocks':statblocks})

def traits_list(request):
    traits = Trait.objects.all().order_by('name')
    return render(request, 'statblocks/traits_list.html', {'traits':traits})

def statblock_page(request, slug):
    statblock = Statblock.objects.get(slug=slug)
    return render(request, 'statblocks/statblocks_page.html', {'statblock':statblock})

@login_required(login_url="/users/login/")
def statblock_new(request):
    if request.method == 'POST':
        form = forms.CreateStatblock(request.POST, request.FILES)
        if form.is_valid():
            new_statblock = form.save(commit=False)
            new_statblock.author = request.user
            new_statblock.save()
            return redirect('statblocks:list')
    else:
        form = forms.CreateStatblock()

    return render(request, 'statblocks/statblock_new.html', {'form':form})