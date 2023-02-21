from rest_framework import serializers

from .models import complaint_model

class complaint_serielizer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = complaint_model
        fields = ('cat_name', 'complaint_title', 'complaint_desc','status', 'address','location')