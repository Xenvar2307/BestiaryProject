from django import forms 
from . import models as myModels
from django.db import models


class CreateStatblock(forms.ModelForm):
    class Meta: 
        model = myModels.Statblock
        fields = ['name','slug','art','description','Sp','WS','BS','S','T','I','Ag','Dex','Int','WP','Fel','HP','Traits']
        
    Traits = forms.ModelMultipleChoiceField(
        queryset=myModels.Trait.objects.all().order_by('name'),
        widget = forms.CheckboxSelectMultiple
    )