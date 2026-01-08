from django.shortcuts import render
from .models import Statblock, Trait

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
