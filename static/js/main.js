$(document).ready(function () {
    $("#generateData").on("click", function () {
        const row_quantity = $("#rowsQuantity").val();
        if (row_quantity === 0 || !row_quantity) {
            $("#rowsInfo").text("value should be > 0")
            return;
        }
        const data = {
            "rows": row_quantity,
        }
        $.ajax({
            url: "/api/schemas/schema/generate/",
            method: "post",
            contentType: "application/json; charset=utf-8",
            data: JSON.stringify(data),
            headers: {
                'X-CSRFToken': $('input[type=hidden][name=csrfmiddlewaretoken]').val()
            },
            success: function (data) {
                $("#rowsInfo").text("success, reload page, please")
                $('#schemas').fadeOut()
            },
            error: function (data) {
                $("#rowsInfo").text("error")
            }
        });
    });
});