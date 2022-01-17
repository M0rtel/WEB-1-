from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'), # Всегда создавать имена для ссылок! Так намного удобнее
    path('about', views.about, name='about')
]