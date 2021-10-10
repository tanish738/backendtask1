from django import forms
from .models import Book
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
#DataFlair
class BookCreate(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'



User=get_user_model()

class CreateUserForm(UserCreationForm):
    class Meta:
        model=get_user_model()
        fields = ('email', 'password1', 'password2','image')
