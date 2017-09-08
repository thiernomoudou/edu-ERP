from rest_framework import serializers

from .models import Student, Baccalaureat, Country, StudentDetail

# from sysadmin.serializers import UserSerializer


class BaccalaureatSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()
    class Meta:
        model = Baccalaureat
        fields = '__all__'
        extra_fields = ['url']



class StudentSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()
    baccalaureat = BaccalaureatSerializer()
    class Meta:
        model = Student
        fields = '__all__'
        extra_fields = ['url']



class CountrySerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()
    
    class Meta:
        model = Country
        fields = '__all__'
        extra_fields = ['url']


class StudentDetailSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()
    # user = UserSerializer()
    country = CountrySerializer()
    student = StudentSerializer()
    class Meta:
        model = StudentDetail
        fields = '__all__'
        extra_fields = ['url']
