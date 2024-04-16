from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='index'),
    path('create/', views.create, name='create'),
    path('update/<id>', views.update, name='update'),
    path('delete/<id>', views.delete, name='delete'),
]