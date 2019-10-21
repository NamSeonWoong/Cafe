from django import forms
from .models import P,C

class PForm(forms.ModelForm):
    class Meta:
        model = P
        fields=('title','content',)

class CForm(forms.ModelForm):
    class Meta:
        model = C
        fields=('content',)
        widgets = {
            'content':forms.TextInput(
                attrs={
                    'placeholder':'comment',
                }
            ),
        }
        labels = {
            'content':'comment',
        }
    