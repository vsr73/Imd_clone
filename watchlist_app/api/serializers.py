from rest_framework import serializers
from watchlist_app.models import *


# def name_len(value):
#     if len(value)<=2:
#         raise serializers.ValidationError("name cannot be smaller")
#     else:HyperlinkedModelSerializer
#         return value
class ReviewSerializer(serializers.ModelSerializer):
    # watchlist=serializers.StringRelatedField()
    class Meta:
        model=Review
        # fields = '__all__'
        exclude=['watchlist']
class WatchListSerializer(serializers.ModelSerializer):
    reviews=serializers.StringRelatedField(many=True,read_only=True)
    class Meta:
        model = WatchList
        fields = '__all__'
        

class StreamingPlatformSerializer(serializers.ModelSerializer):
    # watchlist=WatchListSerializer(many=True,read_only=True)
    # watchlist=serializers.HyperlinkedRelatedField(many=True,read_only=True,
    #                     view_name='movie-detail')
    class Meta:
        model = StreamPlatform
        fields = '__all__'
#for a normal serializer we can apply validations in 2 ways but for model serializer we can do only in one way by creating a function starting with validate and _ and field name for example refer below modle serializer
# class MovieSerializer(serializers.Serializer):
#     id=serializers.IntegerField(read_only=True)
#     name=serializers.CharField(validators=[name_len,])
#     description=serializers.CharField()
#     active=serializers.BooleanField()
#     def create(self,validated_data):
#         # print('\n\n\n\nbefore failing',**validated_data)
#         return Movie.objects.create(**validated_data)
#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.description = validated_data.get('description', instance.description)
#         instance.active = validated_data.get('active', instance.active)
#         instance.save()
#         return instance
#     def validate(self,data):
#         if data['name']==data['description']:
#             raise serializers.ValidationError('name and description cannot be same')
#         else:
#             return data
    # def validate_name(self,value):
    #     # raise serializers.ValidationError("Blog post is not about Django")
    #     if len(value)<=2:
    #         raise serializers.ValidationError("name cannot be smaller")
    #     else:
    #         return value

# class MovieSerializer(serializers.ModelSerializer):
    # len_name=serializers.SerializerMethodField()
    # class Meta:
    #     model = Movie
    #     fields = '__all__'
        # exclude=['name']
    # def get_len_name(self,object):
    #     return len(object.name)
    # def validate_name(self,value):
    #     # raise serializers.ValidationError("Blog post is not about Django")
    #     if len(value)<=2:
    #         raise serializers.ValidationError("name cannot be smaller")
    #     else:
    #         return value