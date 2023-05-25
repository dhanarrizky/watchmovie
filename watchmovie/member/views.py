from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth import authenticate,login, logout
from django.views.generic import CreateView,DeleteView
from videoWatch.models import Video
from .forms import Add_new


# Create your views here.



class homeAdmin(CreateView):
    model = Video
    form_class = Add_new
    template_name = 'homeAdmin.html'
    ordering = ['-id']
    #fields = '__all__'
    
    def get_context_data(self, **kwargs):
        file = Video.objects.all()
        context = super(homeAdmin, self).get_context_data(**kwargs)
        context["file"] = file
        return context
    
    
def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request,username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('hAdmin')
        else:
            return redirect('login')
    else:
        return render(request, 'Registration/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

class delete_video(DeleteView):
    model = Video
    template_name = 'delete_video.html'
    success_url = reverse_lazy('hAdmin')