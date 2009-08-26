$(function()    {

});

// Include ajaxStart() and Stop() functionality
function login()    {//{{{
    var username = $("#id_username").val();
    var password = $("#id_password").val()

    var data = "username=" + username + "&password=" + password;
    var url = "/account/";

    $.ajax({
        url: url,
        type: "POST",
        data: data,
        dataType: "json",

        success: function(response) {
            if (response.code != 0) {
                alert(response.data.body);
            } else  {
                if (response.data.type == "error")  {
                    displayErrors(response.data.body);
                } else  {
                    document.location = "/products/";
                }
            }
        },

        error: function(response)   {
            alert(response);
        }
    });
}//}}}
