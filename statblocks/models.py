from django.db import models
from django.forms.models import model_to_dict

# Create your models here.
class Trait(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.name

class Statblock(models.Model):
    #image?
    name = models.CharField(max_length=50)
    description = models.TextField()
    slug = models.SlugField()

    Sp = models.PositiveSmallIntegerField(default=4)
    WS = models.PositiveSmallIntegerField(default=30)
    BS = models.PositiveSmallIntegerField(default=30)
    S = models.PositiveSmallIntegerField(default=30)
    T = models.PositiveSmallIntegerField(default=30)
    I = models.PositiveSmallIntegerField(default=30)
    Ag = models.PositiveSmallIntegerField(default=30)
    Dex = models.PositiveSmallIntegerField(default=30)
    Int = models.PositiveSmallIntegerField(default=30)
    WP = models.PositiveSmallIntegerField(default=30)
    Fel = models.PositiveSmallIntegerField(default=30)
    HP = models.PositiveSmallIntegerField(default=12)

    Traits = models.ManyToManyField(Trait, blank = True)

    def __str__(self):
        return self.name
