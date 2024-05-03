from django.shortcuts import render

from todo.models import Todo


# Create your views here.

def index_page(request):
    context= {
        'todos': Todo.objects.order_by('priority').all()
    }
    return render(request, 'home/index.html', context)
