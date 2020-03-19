# from django.shortcuts import reverse


# class SetSuccessURLMixin:
#     def get_success_url(self, *args, **kwargs):
#         suffix = 'list'

#         if 'save_add' in self.request.POST:
#             suffix = 'add'

#         elif 'save_edit' in self.request.POST:
#             suffix = 'edit'

#         if suffix == 'edit':
#             return reverse(f'{self.prefix}:{suffix}', args=[self.object.pk])
#         return reverse(f'{self.prefix}:{suffix}')
