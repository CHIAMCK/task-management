from django.db import models


class SoftDeleteManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(
            **{f'{self.model.deleted_field}__isnull': True}
        )
