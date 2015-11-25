from django.shortcuts import render
from recipes.models import Food
from django.shortcuts import render_to_response
from django.template import RequestContext


def food_list(request):
	food = Food.objects.all()
	return render_to_response('recipes/food_list.html', {'object_list': food}, context_instance=RequestContext(request))
