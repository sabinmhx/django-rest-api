# import serializer from rest_framework
from rest_framework import serializers

# import model from models.py
from .models import ApiModel

# Create a model serializer
class ApiSerializer(serializers.HyperlinkedModelSerializer):
	# specify model and fields
	class Meta:
		model = ApiModel
		fields = ('title', 'description')
