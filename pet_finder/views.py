from django.shortcuts import render

def homepage(request):
    return render(request, 'base.html')


def add_pet(request):
    pass

def edit_pet(request, pk):
    pass

def delete_pet(request, pk):
    pass
