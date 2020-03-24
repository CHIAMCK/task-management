import django_filters

from ..models import TeamMember


class TeamMemberFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = TeamMember
        fields = [
            'name'
        ]
