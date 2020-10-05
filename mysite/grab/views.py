from django.shortcuts import render
from django.utils import timezone
from grab.models import Picture

# Create your views here.

def pics_list(request):
    #pics = Picture.objects.filter(author='Hal').order_by('author')
    pics = Picture.objects.all().order_by('author')
    #                                               имя во view
    return render(request, 'grab/pics_list.html', {'pics': pics})
    #                                                      имя переменной 