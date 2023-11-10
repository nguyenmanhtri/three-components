import requests
import logging

from django.contrib.auth.models import User, Group
from django.http import JsonResponse
from django.conf import settings
from rest_framework import viewsets, status
from rest_framework import permissions
from interact_users.serializers.users import UserSerializer, GroupSerializer

logger = logging.getLogger(__name__)


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    # permission_classes = [permissions.IsAuthenticated]
    proxy_url = settings.PROXY_ENDPOINT
    resource = 'users'

    def create(self, request, *args, **kwargs):
        data = request.data.copy()
        url = f'{self.proxy_url}/{self.resource}/'
        proxy_res = requests.post(url, data).json()
        return JsonResponse(proxy_res, status=status.HTTP_201_CREATED, safe=False)

    def list(self, request, *args, **kwargs):
        url = f'{self.proxy_url}/{self.resource}/'
        proxy_res = requests.get(url).json()
        resources = proxy_res.get(self.resource, [])
        res = {
            'count': len(resources),
            'results': resources,
        }
        return JsonResponse(res, safe=False)

    def retrieve(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        if not pk:
            return JsonResponse({'message': 'The requested resource does not exist'}, status=status.HTTP_400_BAD_REQUEST, safe=False)

        url = f'{self.proxy_url}/{self.resource}/{pk}/'
        proxy_res = requests.get(url).json()
        return JsonResponse(proxy_res, safe=False)

    def update(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        if not pk:
            return JsonResponse({'message': 'The requested resource does not exist'}, status=status.HTTP_400_BAD_REQUEST, safe=False)

        data = request.data.copy()
        url = f'{self.proxy_url}/{self.resource}/{pk}/'
        proxy_res = requests.patch(url, data).json()
        return JsonResponse(proxy_res, safe=False)
    
    def destroy(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        if not pk:
            return JsonResponse({'message': 'The requested resource does not exist'}, status=status.HTTP_400_BAD_REQUEST, safe=False)

        url = f'{self.proxy_url}/{self.resource}/{pk}/'
        proxy_res = requests.delete(url).json()
        return JsonResponse(proxy_res, status=status.HTTP_204_NO_CONTENT, safe=False)


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    # permission_classes = [permissions.IsAuthenticated]
