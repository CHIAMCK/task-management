
class RestrictTaskListMixin:

    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset()
        return qs.filter(company_id=self.request.user.team_member.company_id)
