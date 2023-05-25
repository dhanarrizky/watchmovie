from django.shortcuts import render

# Create your views here.
from .models import Video

def index(request):
    if request.method == "GET":
        vid = Video.objects.all().order_by('-id')
        return render (request, 'index.html', {'vid':vid})
    
def watch(request,pk):
    watch = Video.objects.filter(id=pk)
    videos = Video.objects.all()
    return render(request, 'watch.html', {'videos':videos, 'watch':watch})

def search(request):
    if request.method == "POST":
        query = request.POST["search"]
        object_list = Video.objects.filter(name__contains=query)
        return render(request, 'index.html',{'vid':object_list,'search':query})
    else:
        return index