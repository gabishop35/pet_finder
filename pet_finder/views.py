from django.shortcuts import render, redirect, get_object_or_404
from .models import Pet
from pet_finder.forms import PetForm


def homepage(request):
    return render(request, 'base.html')

def info(request):
    return render(request, 'core/info.html')

def add_pet(request):
    if request.method =='POST':
        form = PetForm(request.POST, request.FILES)
        if form.is_valid():
            catch = form.save(commit=False)
            catch.user = request.user
            catch.save()
            return redirect('profile-page')
    else:
        form = PetForm()
    return render(request, 'core/add_pet.html', {'form': form})

def edit_pet(request, pk):
    pet = get_object_or_404(Pet, pk=pk)
    if request.method == 'POST':
        form = PetForm(request.POST, request.FILES, instance=pet)
        if form.is_valid():
            catch = form.save(commit=False)
            catch.user = request.user
            catch.save()
            return redirect('profile-page')
    else: 
        form = PetForm(instance=pet)
    return render(request, 'core/edit_pet.html', {'form': form}) 

def delete_pet(request, pk):
    pet = get_object_or_404(Pet, pk=pk)
    pet.delete()
    return redirect('pet-page')

def profile_page(request):
    pets = Pet.objects.filter(user=request.user)
    return render(request, 'core/profile_page.html', {'pets': pets})