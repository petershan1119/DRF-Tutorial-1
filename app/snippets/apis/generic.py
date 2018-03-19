
from rest_framework import generics, permissions, renderers
from rest_framework.response import Response

from snippets.permissions import IsOwnerOrReadOnly
from utils.pagination import StandardResultsSetPagination
from ..models import Snippet
from ..serializers import SnippetSerializer

__all__ = (
    'SnippetList',
    'SnippetDetail',
)


class SnippetList(generics.ListCreateAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly,
    )

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly,
    )
    pagination_class = StandardResultsSetPagination

class SnippetHighlight(generics.GenericAPIView):
    queryset = Snippet.objects.all()
    renderer_classes = (
        renderers.StaticHTMLRenderer,
    )

    def get(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)