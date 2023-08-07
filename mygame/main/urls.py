# urls.py
from django.urls import path

from . import views

urlpatterns = [
    # path("<int:id>", views.index, name="index"),    
    path('', views.home, name='home'),
    path('round1/', views.round1, name='round1'),
    path('round2/', views.round2, name='round2'),  
    path('account/', views.account, name='account'),      
    path('<str:part_of_speech>/1/', views.show_verb, name='show_verb'),
    path('<str:part_of_speech>/2/', views.show_verb2, name='show_verb2'),
]

