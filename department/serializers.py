from rest_framework import serializers

from .models import ClassLevel, Department, Program


class DepartmentSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()
    class Meta:
        model = Department
        fields = '__all__'
        extra_fields = ['url']


class ClassLevelSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()
    department = DepartmentSerializer()
    class Meta:
        model = ClassLevel
        fields = '__all__'
        extra_fields = ['url']

class ProgramSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()
    department = DepartmentSerializer()
    class Meta:
        model = Program
        fields = '__all__'
        extra_fields = ['url']


