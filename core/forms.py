from django import forms
from .models import Librarian

class LibrarianForm(forms.ModelForm):
    class Meta:
        model = Librarian
        fields = ['name', 'username', 'email', 'password']

