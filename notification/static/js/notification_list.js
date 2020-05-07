import $ from 'jquery'

$(document).ready(() => {
    const url = window.urls.mark_as_read_url
    const data = {
        csrfmiddlewaretoken: window.token.csrfToken
      }
    $.post(url, data)
})
