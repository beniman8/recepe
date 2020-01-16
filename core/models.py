from django.db import models

# Create your models here.

class Recepe(models.Model):
    name = models.TextField()
    prep_time = models.TextField()
    cook_time = models.TextField()
    ready_time = models.TextField()
    snippet = models.TextField()
    pub_date = models.DateTimeField('date published')
    

    def __str__(self):
        return 

class Ingredients(models.Model):
    

    def __str__(self):
        return 

    def __unicode__(self):
        return 


    
