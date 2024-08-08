from django import forms
from .models import Video

class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ('title', 'description', 'video_file')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'style': 'max-width: 600px;'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'style': 'max-width: 600px;'}),
            #'video_url': forms.URLInput(attrs={'class': 'form-control', 'style': 'max-width: 600px;'}),
            'video_file': forms.FileInput(),

        }
