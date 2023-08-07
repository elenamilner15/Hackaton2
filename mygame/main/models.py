from django.db import models

class User(models.Model):    
    username = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=30, unique=True)
    
    score = models.IntegerField(default=0)
    paal_score = models.IntegerField(default=0)
    piel_score = models.IntegerField(default=0)
    hitpael_score = models.IntegerField(default=0)
    hifil_score = models.IntegerField(default=0)
    nifal_score = models.IntegerField(default=0)    
   
    def __str__(self):
        return self.username
    
    
class verbs(models.Model):
    english_word = models.CharField(max_length=30)  
    hebrew_word = models.CharField(max_length=30)
    root = models.CharField(max_length=30) 
    part_of_speech = models.CharField(max_length=30)  
    meaning = models.TextField("")  
    niqqud_stripped_word = models.CharField(max_length=30)
    
    # def __str__(self):
    #     return self.niqqud_stripped_word