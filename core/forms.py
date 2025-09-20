from django import forms
from .models import Librarian
from .models import Library_Member

class LibrarianForm(forms.ModelForm):
    class Meta:
        model = Librarian
        fields = ['name', 'username', 'email', 'password']

class LibraryMemberForm(forms.ModelForm):
    class Meta:
        model = Library_Member
        fields = ['name', 'username', 'DOB', 'address', 'phone', 'email', 'password']

