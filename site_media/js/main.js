$(function()	{

    $(".ajax").ajaxStart(function() {
	$(this).show();
    }).ajaxStop(function()  {
	$(this).hide();
    });

});

function highlightErrorFields(errors)   {
    $('.errorlist').remove();

    if (!errors.keys)	{
	showMessage(errors);
    } else  {
	for (var i=0; i<errors.keys.length; i++) {
	    if (errors.keys[i] == "__all__")    {
		msg = errors.__all__.split("<li>")[1];
		errMsg = msg.split(".")[0];
		showMessage(errMsg);
	    } else  {
		var error_html = errors[errors.keys[i]];
		$("#id_" + errors.keys[i]).parent().before(error_html);
	    }
	}
    }
}

function showMessage(msg)	{
    $("#msger").html("<p>" + msg + "</p>");
    $("#msger").slideDown("fast");
    setTimeout("$('#msger').slideUp('fast')", 7000);
}
