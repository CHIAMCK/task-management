

$(document).ready(() => {
    $('#id_status').change(() => {
        $('#table_form').submit()
    })

    $('[data-clear-on-click]').click(() => {
        target = $($('[data-clear-on-click]').attr('data-clear-on-click'))
        if (target.val()) {
            target.val('')
            $('#table_form').submit()
        }
    })
})