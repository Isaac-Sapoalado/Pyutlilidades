from rest_framework import serializers
from .models import Blog,TagBlog,Comentario,Interacao,Tag

class Blog_serializer(serializers.ModelSerializer):

    tags = serializers.StringRelatedField(many=True,read_only=True)

    class Meta:
        model = Blog
        fields = ['pk','nome','text','publica','dt_created','dt_mod','user','tags']

    
class Comentario_serializer(serializers.ModelSerializer):

    class Meta:
        model = Comentario
        fields = ['text','user','blog']

class Interacao_serializer(serializers.ModelSerializer):

    class Meta:
        model = Interacao
        fields = ['pk','tipo','blog','user']

class TagBlog_serializer(serializers.ModelSerializer):

    class Meta:
        model = TagBlog
        fields = ['pk','blog','tag']
    
class Tag_serializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = ['pk','tag']