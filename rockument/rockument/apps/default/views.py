from django.views import generic
from rest_framework.renderers import JSONRenderer
from rockument.apps.sponge.models import App
from rockument.apps.sponge.serializers import AppSerializer

class HomePageView(generic.ListView):
    model = App
    template_name = 'default/home.html'

    def get_context_data(self, **kwargs):
        kwargs = super().get_context_data(**kwargs)
        serializer = AppSerializer(kwargs.get('object_list'), many=True)
        kwargs.update({
            'object_list': serializer.data
        })
        return kwargs