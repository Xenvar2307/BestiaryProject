from django.shortcuts import render, redirect
from .models import Statblock, Trait
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from . import forms

# Create your views here.
def statblocks_list(request):
    if request.method == 'POST':
        searched_word = request.POST['searched_word']
        searched_author = request.POST['searched_author']
        statblocks = Statblock.objects.all().order_by('name')
        statblocks = statblocks.filter(Q(name__contains= searched_word) | Q(description__contains = searched_word))
        statblocks = statblocks.filter(author__username__contains= searched_author)

        return render(request, 'statblocks/statblocks_list.html', {'statblocks':statblocks, 'searched_word':searched_word, 'searched_author':searched_author})
    else:
        statblocks = Statblock.objects.all().order_by('name')
        return render(request, 'statblocks/statblocks_list.html', {'statblocks':statblocks})

    

def traits_list(request):
    return search_traits_list(request)

def search_traits_list(request):
    if request.method == 'POST':
        searched = request.POST['searched_trait']
        traits = Trait.objects.all().order_by('name').filter(Q(name__contains= searched) | Q(description__contains = searched))

        return render(request, 'statblocks/search_traits_list.html', {'traits':traits, 'searched':searched})
    else:
        traits = Trait.objects.all().order_by('name')
        return render(request, 'statblocks/search_traits_list.html', {'traits':traits})


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
            form.save_m2m()
            return redirect('statblocks:list')
    else:
        form = forms.CreateStatblock()

    return render(request, 'statblocks/statblock_new.html', {'form':form})