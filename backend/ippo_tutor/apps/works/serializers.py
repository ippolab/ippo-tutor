from rest_framework import serializers

from django.core.validators import FileExtensionValidator

from .models import Work


class WorkSerializer(serializers.ModelSerializer):
    document = serializers.FileField(allow_null=True, validators=[FileExtensionValidator(allowed_extensions=['pdf'])])
    source_code = serializers.FileField(allow_null=True, validators=[FileExtensionValidator(allowed_extensions=['zip'])])

    class Meta:
        model = Work
        fields = '__all__'
        read_only_fields = ('id',)
