from django.views import View # Imports the view class
from django.http import HttpResponse #Imports the class for handling HTTP responses
from django.shortcuts import render, redirect #Imports render and redirect functions
from .forms import LibrarianForm #Imports the LibrarianForm from forms.py
from .models import Librarian #Imports the Librarian model from models.py
from .forms import LibraryMemberForm #Imports the LibraryMemberForm from forms.py
from .models import Library_Member #Imports the Library_Member model from models.py

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
            print("Librarian signed up successfully.")
            return redirect('mainscreen')  
    else:
        form = LibrarianForm()
        print(form)
    return render(request, 'core/signup-librarian.html', {'form': form})

def signup_library_member(request):
    if request.method == 'POST':
        form = LibraryMemberForm(request.POST)
        if form.is_valid():
            form.save()
            print("Library member signed up successfully.")
            return redirect('mainscreen')
    else:
        form = LibraryMemberForm()
        print(form)
    return render(request, 'core/signup-library-member.html', {'form': form})

def librarian_list(request):
    librarians = Librarian.objects.all()
    return render(request, 'core/librarian_list.html', {'librarians': librarians})

def librarian_search(request):
    query = request.GET.get('search')
    result = None
    if query:
        result = Librarian.objects.filter(firstname__iexact=query).first()
    return render(request, 'core/librarian_list.html', {'result': result, 'query': query})
