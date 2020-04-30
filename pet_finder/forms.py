from django import forms
from pet_finder.models import Pet

class PetForm(forms.ModelForm):

    class Meta:
        model=Pet
        fields = ('image', 'name', 'animal', 'gender', 'breed', 'color', 'age', 'lost', 'last_seen', 'address', 'city', 'state', 'reward', 'description')