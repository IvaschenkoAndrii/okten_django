from django_filters import rest_framework as filters

from apps.cars.models import CarModel


class CarFilter(filters.FilterSet):
    age_gt = filters.NumberFilter(field_name='age', lookup_expr='gt')
    age_lt = filters.NumberFilter(field_name='age', lookup_expr='lt')
    brand_start = filters.CharFilter(field_name='name', lookup_expr='istartswith')
    brand_end = filters.CharFilter(field_name='name', lookup_expr='endswith')
    brand_contains = filters.CharFilter(field_name='name', lookup_expr='contains')
    price_gt = filters.NumberFilter(field_name='price', lookup_expr='gt')
    price_gte = filters.NumberFilter(field_name='price', lookup_expr='gte')
    price_lt = filters.NumberFilter(field_name='price', lookup_expr='lt')
    price_lte = filters.NumberFilter(field_name='price', lookup_expr='lte')

    class Meta:
        model = CarModel
        fields = ('age_gt', 'age_lt', 'brand_start','brand_end', 'brand_contains','price_gt', 'price_gte', 'price_lt', 'price_lte')
