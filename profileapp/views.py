from django.shortcuts import render
from .forms import ProfileForm
from .models import Profile
# Create your views here.
def home(request):
    if request.method=="POST":
        form = ProfileForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
    form = ProfileForm()
   
    return render(request,'index.html',{'form':form})


def view(request):
    
    prof=Profile.objects.all() 

    return render(request,'view.html',{'prof':prof})
    