$(function()    {
    $("#ajax-loading").hide();

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
    $("#msger").html("<p>" + msg + "</p>");
    $("#msger").slideDown("fast");
    setTimeout("$('#msger').slideUp('fast')", 7000);
}
