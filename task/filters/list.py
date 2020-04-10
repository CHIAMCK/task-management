import django_filters

from ..models import Task
from ..constants.status import STATUS_OPTIONS


class TaskFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    status = django_filters.ChoiceFilter(
        choices=STATUS_OPTIONS,
        empty_label=None
    )

    class Meta:
        model = Task
        fields = [
            'title',
            'status'
        ]
