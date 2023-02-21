from django.db import models

# Create your models here.
from api.categories.models import category_model

class complaint_model(models.Model):
    cat_name = models.ForeignKey(category_model,on_delete=models.CASCADE)
    complaint_title = models.CharField(max_length=120)
    complaint_desc = models.TextField(max_length=254,null=True,blank=True)
    time_of_complaint = models.DateTimeField(auto_now_add=True),
    status = models.CharField(max_length=120,null=True,blank=True)
    address = models.TextField(max_length=254,null=True,blank=True)
    location = models.CharField(max_length=120,null=True,blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.complaint_title
