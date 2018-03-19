from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from ..apis.generic import SnippetList, SnippetDetail

urlpatterns = [
    path('', SnippetList.as_view(), name='snippet-list'),
    path('<int:pk>/', SnippetDetail.as_view(), name='snippet-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)