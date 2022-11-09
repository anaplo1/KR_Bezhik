from rest_framework import serializers


class CompletedDisciplineSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    idStudent = serializers.IntegerField()
    idDiscipline = serializers.IntegerField()
    mark = serializers.CharField(max_length=None, min_length=None, allow_blank=False, trim_whitespace=True)
