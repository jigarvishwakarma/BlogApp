from rest_framework import serializers
from .models import BlogPost,BlogBook

class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = '__all__'
        lookup_field = 'slug'

class BlogBookSerializer(serializers.ModelSerializer):
	class Meta:
		model = BlogBook
		fields = '__all__'
		lookup_field = 'slug'