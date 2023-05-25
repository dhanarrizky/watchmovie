from videoWatch.models import Video
from django import forms


class Add_new(forms.ModelForm):
    class Meta:
        model = Video
        fields = ('name','profile','file','description')
        
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'profile': forms.TextInput(attrs={'class':'form-control','id':'YourId','type':'hidden'}),
            'file': forms.FileInput(attrs={'class':'form-control'}),
            'description': forms.Textarea(attrs={'class':'form-control'}),
        }