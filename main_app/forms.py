from django import forms
from django.forms import ModelForm
from .models import Charging, Shape

class ChargingForm(ModelForm):
  class Meta:
    model = Charging
    fields = ['date', 'method']

class ShapeForm(ModelForm):
  class Meta:
    model = Shape
    fields = ['name', 'formation']


    FORMATION_CHOICES = (
        ('Natural', 'Natural'),
        ('Man-made', 'Man-made'),
    )

    formation = forms.ChoiceField(choices=FORMATION_CHOICES)


