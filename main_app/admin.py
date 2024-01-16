from django.contrib import admin
# import your models here
from .models import Crystal, Charging, Shape, Photo

# Register your models here
admin.site.register(Crystal)
admin.site.register(Charging)
admin.site.register(Shape)
admin.site.register(Photo)