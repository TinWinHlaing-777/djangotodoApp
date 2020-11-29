from django.shortcuts import redirect, render
from .models import Text
from .forms import TaskForm
# Create your views here.

def home(request):
    text = Text.objects.order_by('-id')
    context = {
        'text': text
    }
    if request.method == 'POST':
        post_data = request.POST
        new_text = Text(addtext = post_data['addtext'])
        new_text.save()
        return redirect('/')
    else:
        return render(request, 'home.html', context)

def delete(request,pk):
    delete_data = Text.objects.filter(id=pk)
    delete_data.delete()
    return redirect('/')

def update(request,pk):
    tesk = Text.objects.get(id=pk)
    forms = TaskForm(instance=tesk)
    if request.method == 'POST':
        forms = TaskForm(request.POST, instance=tesk)
        if forms.is_valid():
            forms.save()
            return redirect('/')
    context = {
        'forms': forms
    }
    return render(request, 'update.html',context)

