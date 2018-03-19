from django.urls import path, re_path
from rest_framework.urlpatterns import format_suffix_patterns

from ..apis.api_view import SnippetList, SnippetDetail

urlpatterns = [
    path('', SnippetList.as_view()),
    path('<int:pk>/', SnippetDetail.as_view()),
    # re_path(r'(?P<pk>\d+)/$', SnippetDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)