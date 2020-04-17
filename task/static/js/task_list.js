import $ from 'jquery'

$(document).ready(() => {
    // when user select status, submit the form
    $('#id_status').change(() => {
        $('#table_form').submit()
    })

    // when user click on the clear button, clear the input field and submit the form
    $('[data-clear-on-click]').click(() => {
        target = $($('[data-clear-on-click]').attr('data-clear-on-click'))
        if (target.val()) {
            target.val('')
            $('#table_form').submit()
        }
    })

    // click on the button, send a GET request to backend to get the form layout
    // after get it, render it on the modal body
    $('#add-task-activity-button').click(() => {
        $.ajax({
            method: "GET",
            url: window.urls.task_activity_url,
            success: function(form) {
                console.log(form)
                $('#activities-form').html(form)
            }
        })
    })
})