from crispy_forms.layout import Div, HTML

# <div class="col-sm-6">
#   <div class="card">
#       <div class="card-header"><div>Card title <i class="material-icons align-middle">icon_name</i></div></div>
#           <div class="card-body">
#               <p>hello</p>
#               <p>bye</p>
#           </div>
#       </div>
#   </div>
# </div>


class FormCard(Div):

    def __init__(self, card_title, fields, icon=None):

        icon = f'<i class="material-icons align-middle">{icon}</i>' if icon else ''

        head_div = Div(
            HTML(f'<div>{card_title}{icon}</div>'),
            css_class='card-header'
        )

        body_div = Div(
            *fields,
            css_class='card-body'
        )

        card = Div(
            head_div,
            body_div,
            css_class='card'
        )

        super().__init__(
            card,
            css_class='col-sm-6'
        )
