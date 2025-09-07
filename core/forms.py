from django import forms
from .models import Librarian

class LibrarianForm(forms.ModelForm):
    class Meta:
        model = Librarian
        fields = ['firstname', 'surname', 'email', 'password']

class MemberForm(forms.Form):
    firstname = forms.CharField(max_length=250)
    surname = forms.CharField(max_length=250)
    age = forms.IntegerField(min_value=0)
    email = forms.EmailField()
