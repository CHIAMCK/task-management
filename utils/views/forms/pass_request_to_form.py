
# we can override get_form_kwargs() method to pass request to the form
# get_form_kwargs() is used to build the keyword arguments required
# to instantiate the form

# kwargs={
#   'request': self.request,
#   'data': data,
#   'initial': None
# }


class PassRequestToFormView:
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({'request': self.request})
        return kwargs
