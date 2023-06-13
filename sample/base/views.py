from django.shortcuts import render,HttpResponse
from .forms import SampleForm

# Create your views here.
def home(request):
    form = SampleForm
    context = {
        'form':form
    }

    if request.method == "POST":
        form = SampleForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Successfully Saved')
    
    return render(request,'home.html',context)
  