from django.shortcuts import render , redirect
from Todo_app.models import tasks
from Todo_app.forms import task_forms
from django.contrib import messages
# Create your views here.

def todo_tasks (req):
    if req.method == 'POST':
        form_data = task_forms(req.POST or None)
        if form_data.is_valid():
            form_data.save()
            messages.success(req, 'The Task has been added Sucessfully')
            return redirect('todo_tasks')
        else:
            messages.success(req, 'Something went wrong')
    all_tasks = tasks.objects.all()

    contex = {
        'all_tasks': all_tasks
        }
    return render(req,'todo_tasks.html',contex)

def tasks_delet (req , t_id) :
    task_obj = tasks.objects.get(id=t_id)
    task_obj.delete()
    messages.success(req,f"this task - {task_obj.Task_Name} is deleted ")
    return redirect('todo_tasks')

def tasks_edit (req,t_id):
    task_e = tasks.objects.get(id = t_id)
    
    if req.method == "POST":
        form_data = task_forms(req.POST or None , instance=task_e ) 
        form_data.save()
        messages.success(req, 'The Task has been Updated Sucessfully')
        return redirect('todo_tasks')

    contex = {
        'task_e' : task_e
    }
    return render (req ,'edit_task.html' , contex)

def home (req):
    contex = {
        'page' : 'HOME'
    }
    return render(req,'home.html' , contex)

def services (req):
    contex = {
        'page' : 'SERVICES'
    }
    return render(req,'services.html',contex)

def contact (req):
    contex = {
        'page' : 'CONTACT'
    }
    return render(req,'contact.html',contex)

def about (req):
    contex = {
        'page' : 'ABOUT'}
    return render(req,'contact.html',contex)


        