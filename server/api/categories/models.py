from django.db import models

class category_model(models.Model):
    cat_name = models.CharField(max_length=120)
    dept_name = models.CharField(max_length=120, null=True, blank=True)
    lvl1_title = models.CharField(max_length=120,null=True, blank=True)
    lvl1_email = models.EmailField(max_length=120, null=True, blank=True)
    lvl1_name = models.CharField(max_length=120, blank=True, null=True) 
    lvl2_title = models.CharField(max_length=120,blank=True, null=True)
    lvl2_email = models.EmailField(max_length=120, null=True, blank=True)
    lvl2_name = models.CharField(max_length=120, blank=True, null=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.cat_name
