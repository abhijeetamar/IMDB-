from rest_framework import serializers
from .models import Movie


class MovieSerializer(serializers.ModelSerializer):
    len_name=serializers.SerializerMethodField()
    class Meta:
        model=Movie
        fields='__all__'
        # fields=['name','description']
        # exclude =['name']
    def get_len_name(self,object):
        return len(object.name)

    def validate(self,data):
        if data['name']==data['description']:
            raise serializers.ValidationError('Title and description should be diffrent')
        else:
            return data

    def validate_name(self,value):
        if len(value)<2:
            raise serializers.ValidationError('Name is too short')
        else:
            return value

    # id=serializers.IntegerField(read_only=True)
    # name = serializers.CharField()
    # description = serializers.CharField()
    # active=serializers.BooleanField()

    # def create(self,validated_data):
    #     return Movie.objects.create(**validated_data)#validated data is the new data that user enter in post or put request

    # def update(self,instance,validated_data):#instance carry (old value) and validated data contains (new value)
    #     instance.name=validated_data.get('name',instance.name)
    #     instance.description=validated_data.get('description',instance.description)
    #     instance.active=validated_data.get('active',instance.active)
    #     instance.save()
    #     return instance
