from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from . import models

# Create your views here.
def index(request):
    template = loader.get_template('planes/index.html')
    planes = models.Plane.objects.all().order_by('-capacity')
    context = {
        'planes': planes
    }
    # res = template.render(context)
    return render(request,'planes/index.html',context)


def details(request, plane_id):
    template = loader.get_template('planes/index.html')
    planes = models.Plane.objects.filter(id=plane_id)
    if len(planes) == 0:
        raise models.Plane.DoesNotExist

    context = {
        'planes': planes
    }
    # res = template.render(context)
    return render(request,'planes/index.html',context)


