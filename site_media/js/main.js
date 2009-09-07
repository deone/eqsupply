$(function()    {
    $("#ajax-loading").hide();
    $("#msger").hide();
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

function showMessage(msgType, msg)	{
    if (msgType != "error") {
	$("#msger").html("<p>" + msg + "</p>");
    } else  {
	$("#msger").html("<p class='err'>" + msg + "</p>");
    }
    
    $("#msger").slideDown("fast");
    setTimeout("$('#msger').slideUp('fast')", 5000);
}
