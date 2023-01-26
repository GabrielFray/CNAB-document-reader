from django.urls import path
from . import views

urlpatterns = [
    path("", views.CnabUploadFileView.as_view()),
]
