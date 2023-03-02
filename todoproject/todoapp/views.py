
from django.shortcuts import render
from todoapp.models import TodoListItem
from django.http import HttpResponseRedirect 


# Create your views here.
def todoappView(request):
    all_todo_items = TodoListItem.objects.all()
    return render(request, 'index.html',
    {'all_items':all_todo_items}) 


def addTodoView(request):
    x = request.POST['content']
    if len(x)!=0:
       new_item = TodoListItem(content = x)
       new_item.save()
       return HttpResponseRedirect('/todoapp/') 
    else:
        return HttpResponseRedirect('/todoapp/') 
        

def deleteTodoView(request, i):
    y = TodoListItem.objects.get(id= i)
    y.delete()
    return HttpResponseRedirect('/todoapp/') 