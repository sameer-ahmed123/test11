from django import forms
from testing.models import name,credentials,signup,login

class Nameform(forms.ModelForm):
    class Meta:
        model = name
        fields = '__all__'

class loginForm(forms.ModelForm):
    class Meta:
        model=login
        fields=('Username','Password')
        widgets={'Username':forms.TextInput(attrs={'class':'form-control','placeholder':'Username'}),
                 'Password':forms.TextInput(attrs={'class':'form-control','placeholder':'Password'})}

class CredentialFOrm(forms.ModelForm):
    class Meta:
        model =credentials
        fields=('first_name','last_name','Email','Password' )

        widgets={
            'first_name':forms.TextInput(attrs={'class':'form-control','placeholder':'first name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control','placeholder':'last name'}),
            'Email': forms.EmailInput(attrs={'class': 'form-control','placeholder':'Email@'}),
            'Password': forms.TextInput(attrs={'class': 'form-control','placeholder':'password'})
        }

class Signupform(forms.ModelForm):
    class Meta:
        model=signup
        fields=('Realname','Username','sEmail','sPassword')

