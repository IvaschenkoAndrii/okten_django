from django_filters import rest_framework as filters

from .models import AutoParkModel


class AutoParkFilter(filters.FilterSet):
    cars_age_lt = filters.NumberFilter(field_name='cars__age', lookup_expr='lt')
    name = filters.CharFilter(field_name='name', lookup_expr='endswith')

    class Meta:
        model = AutoParkModel
        # .objects.filter(name__endswith=)
        fields = ('cars_age_lt', 'name')
