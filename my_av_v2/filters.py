from django_filters import BaseInFilter, FilterSet, NumberFilter

from . import models


class NumberInFilter(BaseInFilter, NumberFilter):
    pass


class MovieFilter(FilterSet):
    id__in = NumberInFilter(field_name='id', lookup_expr='in')

    class Meta:
        model = models.Video
        fields = ('id', 'id__in')
