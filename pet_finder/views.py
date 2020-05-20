from django.shortcuts import render, redirect, get_object_or_404
from .models import Pet, FoundPet
from users.models import User
from pet_finder.forms import PetForm, FoundPetForm
from django.contrib.auth.decorators import login_required



def homepage(request):
    return render(request, 'base.html')

def info(request):
    return render(request, 'core/info.html')

@login_required
def add_pet(request):
    if request.method =='POST':
        form = PetForm(request.POST, request.FILES)
        if form.is_valid():
            pet = form.save(commit=False)
            pet.user = request.user
            pet.save()
            return redirect('profile-page')
    else:
        form = PetForm()
    return render(request, 'core/add_pet.html', {'form': form})

@login_required
def edit_pet(request, pk):
    pet = get_object_or_404(Pet, pk=pk)
    if request.method == 'POST':
        form = PetForm(request.POST, request.FILES, instance=pet)
        if form.is_valid():
            pet = form.save(commit=False)
            pet.user = request.user
            pet.save()
            return redirect('profile-page')
    else: 
        form = PetForm(instance=pet)
    return render(request, 'core/edit_pet.html', {'form': form}) 

@login_required
def delete_pet(request, pk):
    pet = get_object_or_404(Pet, pk=pk)
    pet.delete()
    return redirect('profile-page')

@login_required
def profile_page(request):
    pets = Pet.objects.filter(user=request.user)
    return render(request, 'core/profile_page.html', {'pets': pets})

def found_pets(request):
    foundpets = FoundPet.objects.all()
    return render(request, 'core/found_pets.html', {'foundpets': foundpets})

@login_required
def post_found_pet(request):
    if request.method =='POST':
        form = FoundPetForm(request.POST, request.FILES)
        if form.is_valid():
            pet = form.save(commit=False)
            pet.user = request.user
            pet.save()
            return redirect('found-pets')
    else:
        form = FoundPetForm()
    return render(request, 'core/post_found_pet.html', {'form': form})

def lost_pets(request):
    pets = Pet.objects.all()
    return render(request, 'core/lost_pets.html', {'pets': pets})
