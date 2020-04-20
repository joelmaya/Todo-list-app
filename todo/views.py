from django.shortcuts import render,redirect
from django.http import HttpResponse
from.models import todo
from.forms import todoform
from django.views.decorators.http import require_POST

def home(request):
    todo_list=todo.objects.order_by('id')

    form=todoform()
    context={ 'todo_list':todo_list,'form':form}
    return render(request,'todo/base.html',context)

@require_POST
def addtodo(request):
    form=todoform(request.POST)

    print(request.POST['text'])
    if form.is_valid():
        new_todo=todo(text=(request.POST['text']))
        new_todo.save()

    return redirect('todo-home')

def todocompleted(request,todo_id):
    Todo = todo.objects.get(pk=todo_id)
    Todo.complete = True
    Todo.save()

    return redirect('todo-home')

def delete_todo(request):
    todo.objects.filter(complete__exact=True).delete()


    return redirect('todo-home')
def delete_all(request):
    todo.objects.all().delete()

    return redirect('todo-home')




   

  
