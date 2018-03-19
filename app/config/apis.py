from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.views import APIView

from members.serializers import UserSerializer

User = get_user_model()

class APIRoot(APIView):
    def get(self, request, format=None):
        data = {
            'users': reverse('members:user-list', request=request, format=format),
            'snippets': reverse('snippets:snippet-list', request=request, format=format),
        }
        return Response(data)