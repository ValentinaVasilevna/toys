from django.db import models

# Create your models here.
class Material(models.Model):
    name = models.CharField(max_length=20)
    
    def __str__(self):
        return self.name

class Cat(models.Model):
    name = models.CharField(max_length=60)
    
    def __str__(self):
        return self.name


class Toy(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    materials = models.ManyToManyField("Material", related_name="toys")
    image = models.FilePathField(path="toys/static/img")
    #image = models.FilePathField(path="/img")
    last_modified = models.DateTimeField(auto_now=True)
    cat = models.ForeignKey(Cat, on_delete = models.SET_NULL, blank=True, null=True)
    
    def __str__(self):
        return self.title

