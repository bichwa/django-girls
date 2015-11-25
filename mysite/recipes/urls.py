from django.conf.urls import include, url
from recipes.views import food_list

urlpatterns = [

url(r'^food/$', food_list, name='food_list'),


]

