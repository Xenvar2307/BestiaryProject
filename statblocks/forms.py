from django import forms 
from . import models

class CreateStatblock(forms.ModelForm):
    class Meta: 
        model = models.Statblock
        fields = ['name','slug','art','description','Sp','WS','BS','S','T','I','Ag','Dex','Int','WP','Fel','HP','Traits']