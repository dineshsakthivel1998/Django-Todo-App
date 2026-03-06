from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .models import Todo


def index(request):
    if request.method == "POST":
        task = request.POST.get("task")
        if task and task.strip():
            Todo.objects.create(task=task)
        return redirect("index")

    todos = Todo.objects.all()
    return render(request, "todo_main/task2_list.html", {"todos": todos})


def delete(request, id):
    todo = get_object_or_404(Todo, id=id)
    todo.delete()
    return redirect("index")


def edit(request, id):
    todo = get_object_or_404(Todo, id=id)

    if request.method == "POST":
        updated_task = request.POST.get("task")
        if updated_task and updated_task.strip():
            todo.task = updated_task
            todo.save()
            return redirect("index")

    return render(request, "todo_main/edit.html", {"task": todo})

def sampleapi(request):
    return JsonResponse({"message": "API Working"})

def data(request):
    todos = Todo.objects.all()
    return JsonResponse(
        [{"id": t.id, "task": t.task} for t in todos],
        safe=False
    )
    
def toggle_complete(request, id):
    todo = get_object_or_404(Todo, id=id)
    todo.completed = not todo.completed
    todo.save()
    return redirect('index')