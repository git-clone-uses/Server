from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponseNotFound
from .models import *
from .forms import ObjectForm
from .serv import is_server_up, main, a

# Create your views here.
def index(request):
    is_up = serv.is_server_up
    Data = Incoming_Data.objects.all()
    return render(request, 'rango/index.html', context={'Incoming_Data': Data, 'is_up': is_up, 'a': a})

def start_serv(request):
    if(request.GET.get('mybtn')):
        serv.main()
    return HttpResponseRedirect("/")   
        

def objects(request):
    
    Obj = Object.objects.all()
    if (Obj.count() == 0):
        is_null = True
    else:
        is_null = False
        
    return render(request, 'rango/object_main.html', context={'Obj': Obj, 'nll': is_null})

def object_new(request):
    if request.method == "POST":
        form = ObjectForm(request.POST)
        if form.is_valid():
            Object = form.save(commit=False)
            Object.save()
    else:
        form = ObjectForm()
    
    return render(request, 'rango/object_edit.html', {'form': form})    

def delete(request, id):
    try:
        obj = Object.objects.get(id=id)
        obj.delete()
        return HttpResponseRedirect("/objects")
    except Person.DoesNotExist:
        return HttpResponseNotFound("<h2>Object not found</h2>")
    
def edit(request, id):
    try:
        obj = Object.objects.get(id=id)
 
        if request.method == "POST":
            obj.IMEI = request.POST.get("IMEI")
            obj.Gos_Nomer = request.POST.get("Gos_Nomer")
            obj.Description = request.POST.get("Description")
            obj.save()
            return HttpResponseRedirect("/objects")
        else:
            return render(request, "rango/object-edit.html", {"obj": obj})
    except Person.DoesNotExist:
        return HttpResponseNotFound("<h2>Object not found</h2>")
