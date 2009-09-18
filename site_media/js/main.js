function highlightErrorFields(errors)   {
    if (errors.keys)    {
        for (var i=0; i<errors.keys.length; i++) {
	    document.getElementById("id_" + errors.keys[i]).style.background = "#ffa";
        }
    } else  {
        $("#err").html("<ul class='errorlist'><li>" + errors["__all__"] + "</li></ul>");
    }
}

function showMessage(msg)	{
    $("#msger").html("<p>" + msg + "</p>");
    setTimeout("$('#msger').slideUp('fast')", 7000);
}
