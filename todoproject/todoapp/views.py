from django.shortcuts import redirect, render,get_object_or_404
from .models import Todo

def index(request):
    todos = Todo.objects.all()
    context= {"todos": [t for t in todos]}
    return render(request,"index.html",context=context)

def create_task(request):
    task = request.POST["task"]
    todo = Todo(
        created_by =  request.user,
        task = task
    )
    todo.save()
    return redirect("/")

def update_task(request,task_id):
    todo = get_object_or_404(Todo,pk=task_id)
    if todo.is_completed:
        todo.is_completed =False
    else:
        todo.is_completed = True
    todo.save()
    return redirect("/",{"msg":"updated"})

def delete_task(request,task_id):
    todo = get_object_or_404(Todo,pk=task_id)
    todo.delete()
    return redirect("/",{"msg":"delete"})


