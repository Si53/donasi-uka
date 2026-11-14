from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),
    path('kegiatan/<slug:slug>/', views.activity_detail, name='activity_detail'),
]
