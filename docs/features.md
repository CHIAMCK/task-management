
How to add user's company to session when user log in?
when user log in, log out, log in failed, the auth framework will send signal
we can listen to these signals using Signal.connect() method and trigger a function


How to add modal to django template?
1. create a base modal template, define blocks that can be overridden by child templates
2. include the modal template in edit template
3. use jquery to button click event to open a modal


How to use django table 2?
1. use SingleTableMixin, to incorporate a table into a view or template
2. create table class
3. use the django table 2 template tag to render the table


How to exclude soft deleted records?
1. override the get_queryset() of view, add a filter something like date_deleted__isnull=True
    if we override it at view, objetcs.all() will still return all. This is not efficient
    We can actually exclude it at the beginning at model level. override get_queryset() in model Manager

how to auto fill certain fields?
1. modelForm save()
self.form.created_by = self.request.user


How to add datepicker? l
use daterangepicker library
