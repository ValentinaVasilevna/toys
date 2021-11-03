from django.shortcuts import render
from toys.models import Toy, Material, Cat

"""def toy_index(request):
    toys = Toy.objects.all().order_by("-last_modified")  #line 5
    
    for toy in toys:
        toy.image=toy.image[12:]
    
    context = {'toys': toys}
    
    return render(request, 'toy_index.html', context)#line 9
"""
def toy_detail(request, n, pk):
    toy = Toy.objects.get(pk=pk)#line 14
    
    toy.image=toy.image[12:]
    
    materials=toy.materials.all()
    
    context = {
        'toy': toy, 'materials': materials
    }
    return render(request, 'toy_detail.html', context)
	
def cat_index(request):
    cat = Cat.objects.all()
    context = {'cat': cat}
    return render(request, 'cat_index.html', context)

def cat_detail(request, pk):
    cats = Cat.objects.get(pk=pk)
    nm = cats.name
    cat_toys = Toy.objects.all().filter(cat__exact = pk)
    
    for cat_toy in cat_toys:
#        cat_toy.title=cat_toy.title
        cat_toy.image=cat_toy.image[12:]
    
    context = {'cat_toys': cat_toys, 'nm': nm}
    return render(request, 'cat_detail.html', context)