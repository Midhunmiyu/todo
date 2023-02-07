from django.shortcuts import render, redirect

from todoapp import models
from todoapp.forms import todoform
from todoapp.models import todo


# Create your views here.
def index(request):
    return render(request, 'index.html')


def addtodo(request):
    form = todoform()

    if request.method == 'POST':
        form = todoform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view')
    return render(request, 'addtodo.html', {'form': form})


def view(request):
    data = todo.objects.all()
    return render(request, 'view.html', {'data': data})


def delete(request, id):
    # if request.method == 'POST':
        data = todo.objects.get(id=id)
        print(data)
        data.delete()
        return redirect('view')

def update(request,id):
    data=todo.objects.get(id=id)
    form=todoform(instance=data)
    if request.method == 'POST':
        form = todoform(request.POST,instance=data)
        if form.is_valid():
            form.save()
            return redirect('view')
    return render(request, 'addtodo.html', {'form': form})
