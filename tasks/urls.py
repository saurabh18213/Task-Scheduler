from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('new_task/', views.new_task, name='new_task'),
    path('update_task/<int:pk>', views.update_task, name='update_task'),
    path('complete_task/<int:pk>', views.complete_task, name='complete_task'),
    path('remove_task/<int:pk>', views.remove_task, name='remove_task'),
]