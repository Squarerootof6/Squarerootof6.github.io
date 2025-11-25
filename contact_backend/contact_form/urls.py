from django.urls import path
from .views import index, submit_message

urlpatterns = [
    path("", index, name="homepage"),
    path("submit/", submit_message, name="submit_message"),
]
