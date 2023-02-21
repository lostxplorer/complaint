from rest_framework import serializers

from .models import category_model

class category_serielizer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = category_model
        fields = ('cat_name', 'dept_name', 'lvl1_email', 'lvl2_email','lvl1_name', 'lvl2_name')