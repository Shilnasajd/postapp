from django import forms
from myapp.models import Banner

class PostsForm(forms.ModelForm):
    class Meta:
        model=Banner
        fields=["image","post"]
        widgets={
            "image":forms.FileInput(attrs={"class":"form-select"}),
            "post":forms.Textarea(attrs={"class":"form-control","rows":3}),
            
        }
        labels={
            "image":"Image",
            "post":"Description",
            
        }