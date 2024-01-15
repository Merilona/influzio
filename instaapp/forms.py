# myapp/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

# class SignUpForm(UserCreationForm):
#     email = forms.EmailField()

#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password1', 'password2']

class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']



from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
# <!-- template.html -->
# <form method="post" action="{% your_form_action %}">
#     {% csrf_token %}

#     {% for field in form %}
#         <div class="form-group">
#             {{ field }}
#         </div>
#     {% endfor %}

#     <button type="submit" class="btn btn-primary">Register</button>
# </form>
class SignUpForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control form-control-lg','type':'text','placeholder': 'Username', 'required': 'required'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control form-control-lg','type':'email','placeholder': 'Email', 'required': 'required'}))

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control form-control-lg','type':'password','placeholder': 'Password', 'required': 'required'}))
    
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control form-control-lg','type':'password','placeholder': 'Confirm Password', 'required': 'required'}))

    class Meta:
       model = User
       fields = ['username', 'email', 'password1', 'password2']