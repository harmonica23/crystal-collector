import uuid
import boto3
import os
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Crystal, Charging, Shape, Photo
from .forms import ChargingForm, ShapeForm

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def crystals_index(request):
    crystals = Crystal.objects.all() # Retrieve all crystals
    return render(request, 'crystals/index.html', 
    { 
        'crystals': crystals 
    }
)

def crystals_detail(request, crystal_id):
    crystal = Crystal.objects.get(id=crystal_id)
    id_list = crystal.shapes.all().values_list('id')
    shapes_crystal_is_not = Shape.objects.exclude(id__in=id_list)
    charging_form = ChargingForm()
    return render(request, 'crystals/detail.html', {
        'crystal': crystal, 'charging_form': charging_form,
        'shapes': shapes_crystal_is_not
        })

def add_charging(request, crystal_id):
    form = ChargingForm(request.POST)
    if form.is_valid():
        new_charging = form.save(commit=False)
        new_charging.crystal_id = crystal_id
        new_charging.save()
    return redirect('detail', crystal_id=crystal_id)

def add_shape(request):
    shape_form = ShapeForm(request.POST)
    if shape_form.is_valid():
        shape_form.save()
    return redirect('/shapes')


def assoc_shape(request, crystal_id, shape_id):
    Crystal.objects.get(id=crystal_id).shapes.add(shape_id)
    return redirect('detail', crystal_id=crystal_id)

def remove_shape(request, crystal_id, shape_id):
    Crystal.objects.get(id=crystal_id).shapes.remove(shape_id)
    return redirect('detail', crystal_id=crystal_id)

def add_photo(request, crystal_id):
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        try:
            bucket = os.environ['S3_BUCKET']
            s3.upload_fileobj(photo_file, bucket, key)
            url = f"{os.environ['S3_BASE_URL']}{bucket}/{key}"
            print(url)
            Photo.objects.create(url=url, crystal_id=crystal_id)
        except Exception as e:
            print('An error occurred uploading file to S3')
            print(e)
    return redirect('detail', crystal_id=crystal_id)

class CrystalCreate(CreateView):
    model = Crystal
    fields = ['name', 'color', 'appearance', 'rarity', 'source']

class CrystalUpdate(UpdateView):
    model = Crystal
    fields = ['color', 'appearance', 'rarity', 'source']

class CrystalDelete(DeleteView):
    model = Crystal
    success_url = '/crystals'

class ChargingDelete(DeleteView):
    model = Charging
    success_url = '/crystals'

class ShapeList(ListView):
    model = Shape

class ShapeDetail(DetailView):
    model = Shape

# class ShapeCreate(CreateView):
#     model = Shape
#     fields = '__all__'

class ShapeCreate(CreateView):
    model = Shape
    form_class = ShapeForm
    template_name = 'main_app/shape_form.html' 
    success_url = '/shapes'

class ShapeUpdate(UpdateView):
    model = Shape
    fields = '__all__'

class ShapeDelete(DeleteView):
    model = Shape
    success_url = '/shapes'