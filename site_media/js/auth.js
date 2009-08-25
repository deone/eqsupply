$(function()    {

});

function login()    {//{{{
    var username = $("#id_username").val();
    var password = $("#id_password").val()

    var data = "username=" + username + "&password=" + password;
    var url = "/account/login/";

    $.ajax({
        url: url,
        type: "POST",
        data: data,
        dataType: "json",

        success: function(response) {
            alert(response.data.type);
        },

        error: function(response)   {
            alert(response);
        }
    });
}//}}}
