from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=20)
    doctorChoices=(
        ('1','Dr Arnav Osborne'),
        ('2','Dr Muskan Singh'),
        ('3','Dr Morgan Hester'),
        ('4','Dr Suraj Sandal'),
        ('5','Dr Sanjit Nayar'),
        ('6','Dr Aahana Kaur')
    )
    DName = models.CharField(max_length=1,default='1',choices=doctorChoices)
    issue = models.TextField()
    date =models.DateField()
