from django.urls import path
from . import views
	
urlpatterns = [
	path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('crystals/', views.crystals_index, name='index'),
    path('crystals/<int:crystal_id>/', views.crystals_detail, name='detail'),
    path('crystals/create/', views.CrystalCreate.as_view(), name='crystals_create'),
    path('crystals/<int:pk>/update/', views.CrystalUpdate.as_view(), name='crystals_update'),
    path('crystals/<int:pk>/delete/', views.CrystalDelete.as_view(), name='crystals_delete'),
    path('crystals/<int:crystal_id>/add_charging/', views.add_charging, name='add_charging'),
    path('charging/<int:pk>/delete/', views.ChargingDelete.as_view(), name='charging_delete'),
    path('shapes/', views.ShapeList.as_view(), name='shapes_index'),
    path('shapes/<int:pk>/', views.ShapeDetail.as_view(), name='shapes_detail'),
    path('shapes/create/', views.ShapeCreate.as_view(), name='shapes_create'),
    path('shapes/<int:pk>/update/', views.ShapeUpdate.as_view(), name='shapes_update'),
    path('shapes/<int:pk>/delete/', views.ShapeDelete.as_view(), name='shapes_delete'),
    path('crystals/<int:crystal_id>/assoc_shape/<int:shape_id>/', views.assoc_shape, name='assoc_shape'),
    path('crystals/<int:crystal_id>/remove_shape/<int:shape_id>/', views.remove_shape, name='remove_shape'),
    path('crystals/<int:crystal_id>/add_photo/', views.add_photo, name='add_photo'),
]