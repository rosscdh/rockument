from rest_framework import generics

from rockument.apps.sponge.models import Revision

class AppRevisionsViewSet(generics.ListAPIView):
    """
    A simple ViewSet for viewing accounts.
    """
    queryset = Revision.objects.all()
    serializer_class = AccountSerializer

    def list(self, request, *args, **kwargs):
        pass