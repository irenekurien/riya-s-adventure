from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse

from .models import Todo
from .forms import ToDoForm

# Create your views here.


def home(request):
    if request.method == 'GET':
        return render(request, 'home.html', {'form': ToDoForm()})
    else:
        try:
            form = ToDoForm(request.POST)
            print(form)
            form.save()
            return redirect('viewtodo')
        except ValueError:
            return render(request, 'home.html', {'form': ToDoForm(), 'error': 'Choose a smaller title'})


def viewtodo(request):
    context = {}
    todo = Todo.objects.all()
    context['todos'] = todo
    return render(request, 'views.html', context)
    #  return HttpResponse("This is the home Page")


def updatetodo(request, todo_pk):
    todo = get_object_or_404(Todo, pk=todo_pk)
    if request.method == "GET":
        form = ToDoForm(instance=todo)
        return render(request, 'update.html', {'form': form})
    elif request.method == "POST":
        form = ToDoForm(request.POST, instance=todo)
        form.save()
        return redirect('viewtodo')
