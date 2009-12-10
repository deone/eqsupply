$(function()	{

    $(".ajax").ajaxStart(function() {
	$(this).show();
    }).ajaxStop(function()  {
	$(this).hide();
    });

});

function highlightErrorFields(errors)   {
    for (var i=0; i<errors.keys.length; i++) {
	if (errors.keys[i] == "__all__")    {
	    showMessage(errors.__all__);
	} else	{
	    document.getElementById("id_" + errors.keys[i]).style.background = "#ffa";
	}
    }
}

function showMessage(msg)	{
    $("#msger").html("<p>" + msg + "</p>");
    $("#msger").slideDown("fast");
    setTimeout("$('#msger').slideUp('fast')", 7000);
}
