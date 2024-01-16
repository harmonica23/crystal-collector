from django.db import models
from django.urls import reverse

FORMATION_CHOICES = [
    ('Natural', 'Natural'),
    ('Cut', 'Cut'),
]

METHODS = (
    ('FM', 'Full Moon'),
    ('SL', 'Sun Light'),
    ('So', 'Sound'),
    ('Se', 'Selenite'),
    ('Sm', 'Smudge'),
    ('Wa', 'Water'),
)

# Create your models here.
    
class Shape(models.Model):
    name = models.CharField(max_length=50)
    formation = models.CharField(
        max_length=100, 
        choices=FORMATION_CHOICES, 
        default='Natural'
        )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shapes_detail', kwargs={'pk': self.id})
    
class Crystal(models.Model):
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    appearance = models.TextField(max_length=500)
    rarity = models.CharField(max_length=100)
    source = models.TextField(max_length=250)
    shapes = models.ManyToManyField(Shape)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'crystal_id': self.id})
    
class Charging(models.Model):
    date = models.DateField('Charging Date')
    method = models.CharField(
        max_length=100,
        choices=METHODS,
        default=METHODS[0][0]
        )
    crystal = models.ForeignKey(Crystal, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_method_display()} on {self.date}"
    
    class Meta:
        ordering = ['-date']

    

class Photo(models.Model):
    url = models.CharField(max_length=200)
    crystal = models.ForeignKey(Crystal, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for crystal_id: {self.crystal_id} @{self.url}"