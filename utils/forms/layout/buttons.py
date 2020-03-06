from crispy_forms.layout import ButtonHolder, Submit, Button

# <div class=”buttonHolder”>
#   <input type="submit" name="save" value="Save" class="btn white btn-success" />
#   <input type="submit" name="save_add" value="Save and add" class="btn white" />
#   <input type="submit" name="submit_cancel" value="Cancel" class="btn white btn-link" />
# </div>


class SubmitButtonsGroup(ButtonHolder):
    def __init__(self, *buttons, css_class, button_css_classes):
        super().__init__(
            *[
                Submit(
                    button[0], button[1],
                    css_class=f'{css_class} {button_css_classes.get(button[0],"")}'
                )
                if button[0] != 'submit_cancel' else
                Button(
                    button[0], button[1],
                    css_class=button_css_classes.get('submit_cancel', 'btn-link')
                )
                for button in buttons
            ]
        )


class SubmitButtons(SubmitButtonsGroup):
    def __init__(self):

        button_css_classes = {
            'save': 'btn-success',
            'save_add': '',
            'save_edit': ''
        }

        css_class = 'btn white'

        buttons = [
            ('save', 'Save'), ('save_add', 'Save and add'),
            ('submit_cancel', 'Cancel')
        ]

        super().__init__(*buttons, css_class=css_class, button_css_classes=button_css_classes)


class EditSubmitButtons(SubmitButtonsGroup):

    def __init__(self, delete=True):
        css_class = 'btn white'
        button_css_classes = {
            'save': 'btn-success',
            'save_edit': '',
            'delete': 'btn-danger'
        }

        buttons = [('save', 'Save'), ('save_edit', 'Save and edit')]

        if delete:
            buttons.append(('delete', 'Delete'))

        buttons.append(('submit_cancel', 'Cancel'))

        super().__init__(
            *buttons,
            css_class=css_class,
            button_css_classes=button_css_classes
        )
