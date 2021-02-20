from django.dispatch import Signal, receiver
from django.template.defaultfilters import slugify

import uuid


def _model_slug_exists(model, queryset=None, **kwargs):
    #
    # allow override of queryset
    #
    queryset = model.objects if queryset is None else queryset
    try:
        return queryset.get(**kwargs)
    except model.DoesNotExist:
        return None
    except model.MultipleObjectsReturned:
        #
        # in case we have the same key (which we do in a few cases)
        #
        return None


def ensure_slug(sender, **kwargs):
    """
    signal to handle creating the workspace slug
    """
    instance = kwargs.get('instance')

    if instance.slug in [None, '']:

        final_slug = slugify(instance.name)[:32]

        while _model_slug_exists(model=instance.__class__.objects.model, slug=final_slug):
            # logger.info(f"Instance {final_slug} exists, trying to create another")
            slug = '%s-%s' % (final_slug, uuid.uuid4().get_hex()[:4])
            slug = slug[:30]
            final_slug = slugify(slug)

        instance.slug = final_slug

