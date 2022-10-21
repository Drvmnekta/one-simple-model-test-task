"""Module with mixins."""

from rest_framework import mixins, viewsets


class CreateListViewSet(mixins.CreateModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    """Viewset mixin for create and list methods."""
    
    pass
