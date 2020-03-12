import $ from 'jquery'
import 'daterangepicker'

$(document).ready(() => {
    $('#id_due_date').daterangepicker({
        singleDatePicker: true,
        timePicker: true,
        autoUpdateInput: false,
        locale: {
            format:'YYYY-MM-DD HH:mm' ,
            cancelLabel: 'Clear'
        }
    })

    $('#id_due_date').on('apply.daterangepicker', function(ev, picker) {
        $(this).val(picker.endDate.format('YYYY-MM-DD HH:mm'))
    })
})
