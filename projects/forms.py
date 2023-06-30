from django.forms import ModelForm 
from django import forms 
from .models import Project, Review



class ProjectForm(ModelForm):
    class Meta:
        model = Project 
        fields = ['title', 'image','description', 'code_link', 'demo_link']
        widgets={
            'tags':forms.CheckboxSelectMultiple(),
        }

    image = forms.FileField(label="Upload Project Image",
                widget=forms.ClearableFileInput(
                    attrs={
                    'style': 'font-size: 16px',
                    'accept': 'image/png, image/jpg'
                }
                )                            
 )

    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)

        self.fields['title'].widget.attrs.update({'class':'input', "placeholder":'project title'})
        
        self.fields['description'].widget.attrs.update({'class':'input', "placeholder":'about project'})

        self.fields['demo_link'].widget.attrs.update({'class':'input', "placeholder":'Live link'})

        self.fields['code_link'].widget.attrs.update({'class':'input', "placeholder":'github repo'})

    
    

class ReviewForm(ModelForm):
    class Meta:
        model = Review 
        fields = ['value', 'body']

        labels ={
            'value': 'Vote for the project',
            'body': 'Leave a review'
        }

    def __init__(self, *args, **kwargs):
        super(ReviewForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'input'})
