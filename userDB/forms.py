from django import forms
from userDB.models import user

class UserForm(forms.ModelForm):
    class Meta:
        model = user
        fields= ["name","height","weight","dietary_preference"]
        exclude= []
