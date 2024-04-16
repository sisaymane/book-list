from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .forms import BookForm
from .models import Book

# Create your views here.
def home(request):
    books = Book.objects.all()
    return render(request, 'index.html', { 'books': books })

def create(request):
    form = BookForm(request.POST or None)
    if form.is_valid():
        # instance = form.save(commit=False)
        # instance.save()
        form.save()
        return redirect('index')
    context = {
        "form": form
    }
    return render(request, 'create_forms.html', context)

def update(request, id=None):
    instance = get_object_or_404(Book, id=id)
    form = BookForm(request.POST or None, instance=instance)
    if form.is_valid():
        instance= form.save(commit=False)
        instance.save()
        return redirect('index')
    context = {
        "form": form,
    }
    return render(request, 'update_forms.html', context)

def delete(request, id=None):
    instance = get_object_or_404(Book, id=id)
    instance.delete()
    return redirect('index')