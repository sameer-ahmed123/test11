from django import forms
from testing.models import signup


class Signupform(forms.ModelForm):
    class Meta:
        model=signup
        fields=('Realname','Username','sEmail','sPassword')

