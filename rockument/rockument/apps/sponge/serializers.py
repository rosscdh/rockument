from rest_framework import serializers
from .models import App, Revision


class RevisionSerializer(serializers.ModelSerializer):
    url = serializers.URLField(source='get_url')
    class Meta:
        model = Revision
        fields = ['pk',
                  'revision',
                  'repo',
                  'url',
                  'created',
                  'updated',]


class AppSerializer(serializers.ModelSerializer):
    num_revisions = serializers.SerializerMethodField()
    latest_revisions = RevisionSerializer(source='revision_set', many=True)
    url = serializers.URLField(source='get_url')
    class Meta:
        model = App
        fields = ['id',
                 'slug',
                 'name',
                 'num_revisions',
                 'latest_revisions',
                 'url']

    def get_num_revisions(self, obj) -> int:
        return obj.revision_set.count()