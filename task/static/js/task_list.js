import $ from 'jquery'

$(document).ready(() => {

    let currentTaskId

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

    // submit form, POST request
    // if there is data, send POST request

    const taskActivityModalForm = $('#activities-form')

    taskActivityModalForm.delegate('form', 'submit', async (e) => {
        e.preventDefault()
        const url = $(e.target).attr('action')
        const data = new FormData(e.target)
        $.ajax({
            method: "POST",
            data,
            processData: false, // pass form data using FormData()
            contentType: false, // pass form data using FormData()
            url: url,
            success: function(form) {
                taskActivityModalForm.html(form)
            }
        })
    })

    $('[data-target="#add-task-activity-modal"').click(({ target }) => {
        currentTaskId = $(target).attr('data-task-id')
        const url = window.urls.task_activity_url.replace('0', currentTaskId)

        $.ajax({
            method: "GET",
            url,
            success: function(form) {
                taskActivityModalForm.html(form)
            }
        })
    })
})