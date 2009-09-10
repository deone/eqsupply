$(function()    {

    $("#ajax-loading").ajaxStart(function()	{
	$(this).show();
    }).ajaxStop(function()   {
	$(this).hide();
    });
});

function displayErrors(errors)   {
    if (errors.keys)    {
        for (var i=0; i<errors.keys.length; i++) {
            $("#id_" + errors.keys[i]).before("<ul class='errorlist'><li>" + errors[errors.keys[i]] + "</li></ul>");
        }
    } else  {
        $("#err").html("<ul class='errorlist'><li>" + errors["__all__"] + "</li></ul>");
    }
}

function showMessage(msg)	{
    $("#message").html("<p>" + msg + "</p>");
    $("#message").slideDown("fast");
    setTimeout("$('#message').slideUp('fast')", 7000);
}
