from rest_framework import serializers

from .models import AcademicYear, Admission, AdmissionProcess

from student.serializers import StudentSerializer
from department.serializers import ClassLevelSerializer

class AcademicYearSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()
    class Meta:
        model = AcademicYear
        fields = '__all__'
        extra_fields = ['url']

class AdmissionSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()
    academic_year = AcademicYearSerializer()
    student = StudentSerializer()
    class_level = ClassLevelSerializer()

    class Meta:
        model = Admission
        fields = '__all__'
        extra_fields = ['url']


class AdmissionProcessSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()
    # user = UserSerializer()
    admission = AdmissionSerializer()

    class Meta:
        model = AdmissionProcess
        fields = '__all__'
        extra_fields = ['url']