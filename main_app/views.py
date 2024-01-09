from django.shortcuts import render

crystals = [
    {'name': 'Labradorite', 'color': 'multi', 'appearance': 'iridescent blue or gold flashes', 'rarity': 'readily available', 'source': 'Italy, Greenland, Finland, Russia, Canada, Scandanavia'},
    {'name': 'Azurite', 'color': 'deep blue', 'appearance': 'very small, shiny crystals', 'rarity': 'easily obtained, often in combination with malachite', 'source': 'USA, Australia, Chile, Peru, France, Namiba, Russia, Egypt'},
    {'name': 'Rose Quartz', 'color': 'pink', 'appearance': 'usually translucent', 'rarity': 'easily obtained', 'source': 'S. Africa, USA, Brazil, Japan, India, Madagascar'},
    {'name': 'Carnelian', 'color': 'red, orange, pink, brown', 'appearance': 'small, translucent pebble often water-worn', 'rarity': 'common', 'source': 'Britian, India, Czech Republic, Slovakia, Peru, Iceland, Romania'},
]

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def crystals_index(request):
    return render(request, 'crystals/index.html', {
        'crystals': crystals
    })