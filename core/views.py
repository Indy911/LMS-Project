from django.views import View # Imports the view class
from django.http import HttpResponse #Imports the class for handling HTTP responses
from django.shortcuts import render, redirect #Imports render and redirect functions
from .forms import LibrarianForm
from .models import Librarian

# Create your views here.
def home(request):
    return render(request, 'core/mainscreen.html')

def loginmain(request):
    return render(request, 'core/login-mainpage.html')

def signupmain(request):
    return render(request, 'core/signup-mainpage.html')

def signuplibrarian(request):
    return render(request, 'core/signup-librarian.html')

def signup_librarian(request):
    if request.method == 'POST':
        form = LibrarianForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('librarian_list')  # or wherever you want
    else:
        form = LibrarianForm()
        print(form)
    return render(request, 'core/signup-librarian.html', {'form': form})

def librarian_list(request):
    librarians = Librarian.objects.all()
    return render(request, 'core/librarian_list.html', {'librarians': librarians})

def librarian_search(request):
    query = request.GET.get('search')
    result = None
    if query:
        result = Librarian.objects.filter(firstname__iexact=query).first()
    return render(request, 'core/librarian_list.html', {'result': result, 'query': query})
