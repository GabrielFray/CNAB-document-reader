from rest_framework.serializers import Serializer, FileField


class CnabUploadFileSerializer(Serializer):
    file_upload = FileField()

    class Meta:
        fields = "__all__"