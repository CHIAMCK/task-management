
// anonymous functions
// Functions stored in variables do not need function names.
// They are always invoked (called) using the variable name.
export const getTaskActivitiesForm = (url, taskActivityModalForm) => {

    return new Promise(resolve => {
        $.ajax({
            method: "GET",
            url,
            success: function(form) {
                taskActivityModalForm.html(form)
                resolve()
            }
        })
    })
}

export const loadTaskActivity = async(target, currentTaskId) => {
    const url = window.urls.get_task_activity_url.replace('0', currentTaskId)
    return new Promise(resolve => target.load(url, () => resolve()))
}

