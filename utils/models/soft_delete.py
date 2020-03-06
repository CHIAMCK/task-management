from django.utils import timezone


class SoftDeleteModel():
    deleted_field = 'deleted_date'

    def delete(self, using=None, keep_parents=None):
        setattr(self, self.deleted_field, timezone.now())
        self.save()
