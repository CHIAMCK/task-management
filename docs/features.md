
How to add user's company to session when user log in?
1. when user log in, log out, log in failed, the auth framework will send signal
2. we can listen to these signals using Signal.connect() method and trigger a function


How to add modal to django template?
1. create a base modal template, define blocks that can be overridden by child templates
2. include the modal template in edit template
3. use jquery to button click event to open a modal


How to use django table 2?
1. use SingleTableMixin, to incorporate a table into a view or template
2. create table class
3. use the django table 2 template tag to render the table, {% render_table table %}


How to exclude soft deleted records?
1. override the get_queryset() of view, add a filter something like date_deleted__isnull=True
    if we override it at view, objetcs.all() will still return all. This is not efficient
    We can actually exclude it at the beginning at model level. override get_queryset() in model Manager

how to auto fill certain fields?
1. modelForm save()
self.form.created_by = self.request.user


How to add datepicker?
1. use daterangepicker library
2. use jQuery to customize it

How to add modal?
1. create a base modal template, with blocks to enable user to customize it
2. create a modal using the base modal template
3. include it in the template
4. use jquery to open the modal

How to customized success url based on which button is pressed?
1. there is a method caled get_success_url() that will determine the success url
2. we can override this method and check the request.
3. when the button is pressed, it will pass the name and value of input field in the request
4. check which button is pressed and based on that decide the url

How to add filter to table?
1. use django filter
2. use the Filterview (provide model and filterset_class)
3. use filterset to create filter, generate filter based on model's fields,
there are many filters we can choose exp: CharFilter, BooleanFilter, ChoiceFilter ...
4. wrap the card inside a form
5. add the input for filter in the template, filter.form.<field_name>



How to create custom django command?
1. create folder management/command/<your_file>
2. can pass arguments when you run the command, example: ./manage.py cleanup_data --days=30 --commit
3. don't use print() in script, use  ---> self.stdout.write(self.style.SUCCESS("Getting User"))
4. can check the execution time, example
   def some_method:
        start_time = time.time()
        self.stdout.write(self.style.WARNING("--- %s seconds ---\n" % (time.time() - start_time)))
5. can start a SQL transaction, @transaction.atomic, which allows user to dry run (run without committing changes to DB) the script.

How to delete file in FileField?
1. call the delete() of the FileField instance, example: instance.document.delete(False), False means that don't save the instance
2. can use with post_delete signal to delete the instance and the file associates with it
