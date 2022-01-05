from django import forms
from testing.models import name,credentials,signup

class Nameform(forms.ModelForm):
    class Meta:
        model = name
        fields = '__all__'

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

