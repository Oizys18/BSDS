from django import forms
from .models import FoundPosting, FoundImage


class FoundPostingForm(forms.ModelForm):

    class Meta:
        model = FoundPosting
        fields = ('content', 'status', 'has_img')


class FoundImageForm(forms.ModelForm):
    class Meta:
        model = FoundImage
        fields = ('image', 'thumbnail')
        widgets = {
            'image': forms.FileInput(attrs={'multiple': True}),
            'thumbnail': forms.FileInput(attrs={'multiple': True}),
        }
