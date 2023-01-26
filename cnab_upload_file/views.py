from utils.normalize import normalize_file_txt
from .serializers import CnabUploadFileSerializer
from rest_framework.generics import ListCreateAPIView
from cnab_transactions.models import CnabTransactions
from cnab_transactions.serializers import filter_store
from cnab_transactions.serializers import CnabTransactionsSerializer


class CnabUploadFileView(ListCreateAPIView):
    serializer_class = CnabTransactionsSerializer

    def get_queryset(self):
        store = filter_store(CnabTransactions.objects.all())
        return store

    def get_serializer_class(self):
        if self.request.method == "GET":
            return CnabTransactionsSerializer
        elif self.request.method == "POST":
            return CnabUploadFileSerializer

    def perform_create(self, serializer):
        upload_file = self.request.FILES["file_upload"]
        normalize_file_txt(upload_file)
